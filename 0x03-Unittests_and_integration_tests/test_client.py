#!/usr/bin/env python3
"""python module"""
from client import GithubOrgClient
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Tests the `GithubOrgClient` class."""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org method of GithubOrgClient class"""
        mock_get_json.return_value = {"login": org_name}
        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
            )
        self.assertEqual(result, {"login": org_name})

    def test_public_repos_url(self):
        """ Mock payload for the org property"""
        mock_org_payload = {
                "repos_url": "https://api.github.com/orgs/test_org/repos"
            }

        with patch(
                'client.GithubOrgClient.org', new_callable=PropertyMock
            ) as mock_org:
            # Set the return value of the mocked org property
            mock_org.return_value = mock_org_payload

            client = GithubOrgClient("test_org")
            result = client._public_repos_url

            # Check that the result is as expected
            self.assertEqual(
                    result, "https://api.github.com/orgs/test_org/repos"
                )

            # Verify that the org property was accessed exactly once
            mock_org.assert_called_once()


if __name__ == "__main__":
    unittest.main()
