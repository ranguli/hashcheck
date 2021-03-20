import pytest

from ioccheck.exceptions import InvalidHashException
from ioccheck.iocs import Hash
from ioccheck.types import MD5, SHA256


class TestHashCreation:
    """ Instantiating Hash() objects """

    class TestHashCreationEICAR:
        def test_ioccheck_eicar_sha256_implicit(self, ioccheck_eicar_sha256_implicit):
            """ Hashcheck correctly guesses a SHA256"""
            assert ioccheck_eicar_sha256_implicit.hash_type == SHA256

        def test_ioccheck_eicar_sha256_explicit(self, ioccheck_eicar_sha256_explicit):
            """ Hashcheck explicitly accepts a SHA256"""
            assert ioccheck_eicar_sha256_explicit.hash_type == SHA256

        def test_ioccheck_eicar_md5_implicit(self, ioccheck_eicar_md5_implicit):
            """ Hashcheck correctly guesses an MD5"""
            assert ioccheck_eicar_md5_implicit.hash_type == MD5

        def test_ioccheck_eicar_md5_explicit(self, ioccheck_eicar_md5_explicit):
            """ Hashcheck correctly guesses an MD5"""
            assert ioccheck_eicar_md5_explicit.hash_type == MD5

    class TestHashCreationClean:
        def test_ioccheck_clean_sha256_implicit(self, ioccheck_clean_sha256_implicit):
            """ Hashcheck correctly guesses a SHA256"""
            assert ioccheck_clean_sha256_implicit.hash_type == SHA256

        def test_ioccheck_clean_sha256_explicit(self, ioccheck_clean_sha256_explicit):
            """ Hashcheck explicitly accepts a SHA256"""
            assert ioccheck_clean_sha256_explicit.hash_type == SHA256

        def test_ioccheck_clean_md5_implicit(self, ioccheck_clean_md5_implicit):
            """ Hashcheck correctly guesses an MD5"""
            assert ioccheck_clean_md5_implicit.hash_type == MD5

        def test_ioccheck_clean_md5_explicit(self, ioccheck_clean_md5_explicit):
            """ Hashcheck correctly guesses an MD5"""
            assert ioccheck_clean_md5_explicit.hash_type == MD5

    class TestInvalidHashExceptions:
        @pytest.mark.parametrize(
            "file_hash,hash_type",
            [
                ("12345", MD5),
                ("12345", SHA256),
                ("", MD5),
                ("", SHA256),
                (1, SHA256),
                (1, MD5),
                (1, None),
                (None, SHA256),
                (None, MD5),
                (SHA256, None),
                (SHA256, ""),
                (MD5, None),
                ([], SHA256),
                ([], MD5),
                ([], None),
                ({}, None),
                ("abc", None),
                ("abc", MD5),
                ("abc", SHA256),
            ],
        )
        def test_invalid_hash_exception(self, file_hash, hash_type):
            with pytest.raises(InvalidHashException):
                Hash(file_hash, hash_type)
