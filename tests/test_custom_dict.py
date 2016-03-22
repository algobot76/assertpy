# Copyright (c) 2015-2016, Activision Publishing, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from assertpy import assert_that


def test_custom_dict():
    d = CustomDict({
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'User-Agent': 'python-requests/2.9.1'})

    assert_that(d).is_not_none()

    assert_that(d.keys()).contains('Accept-Encoding', 'Connection', 'Accept', 'User-Agent')
    assert_that(d).contains_key('Accept-Encoding', 'Connection', 'Accept', 'User-Agent')

    assert_that(d.values()).contains('gzip, deflate', 'keep-alive', 'application/json', 'python-requests/2.9.1')
    assert_that(d).contains_value('application/json')

    assert_that(d['Accept']).is_equal_to('application/json')
    assert_that(d).contains_entry({'Accept':'application/json'})


def test_requests():
    try:
        import requests
        d = requests.structures.CaseInsensitiveDict({
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'User-Agent': 'python-requests/2.9.1'})

        assert_that(d).is_not_none()

        assert_that(d.keys()).contains('Accept-Encoding', 'Connection', 'Accept', 'User-Agent')
        assert_that(d).contains_key('Accept-Encoding', 'Connection', 'Accept', 'User-Agent')

        assert_that(d.values()).contains('gzip, deflate', 'keep-alive', 'application/json', 'python-requests/2.9.1')
        assert_that(d).contains_value('application/json')

        assert_that(d['Accept']).is_equal_to('application/json')
        assert_that(d).contains_entry({'Accept':'application/json'})
    except ImportError:
        pass


class CustomDict():

    def __init__(self, d):
         self._dict = d
         self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
         try:
             result = self.keys()[self._idx]
         except IndexError:
             raise StopIteration
         self._idx += 1
         return result

    def __contains__(self, key):
        return key in self.keys()

    def keys(self):
        return list(self._dict.keys())

    def values(self):
        return list(self._dict.values())

    def __getitem__(self, key):
        return self._dict.get(key)

