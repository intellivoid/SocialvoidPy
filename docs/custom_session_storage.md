# Custom Session Storage

You can use a different method of storing session data in case if you don't want an unencrypted file of the session laying around.
The session data is only updated whenever `session.create` is called. See also: [examples/custom_session.py](https://github.com/Intellivoid/SocialvoidPy/blob/master/examples/custom_session.py)

```python
>>> sv = SocialvoidClient()
>>> sv.session.create()
>>> sv.session.get()
Session(id='35714fd511b6064908da4ed77c12f587-79c2f3c3-2036-4f3e-9db2-efd52118c06c-0d981a4d', flags=[], authenticated=False, created=datetime.datetime(2021, 10, 6, 20, 13, 28), expires=datetime.datetime(2021, 10, 6, 20, 23, 28))
>>> (sv.session.public_hash, sv.session.private_hash, sv.session.session_id, sv.session.session_challenge, sv.session.session_exists)
('5ee8486fa6a9c7d4bdd234efdfa9099ae2ef5ab0d9aff77c004caf22d11e9c77', '1746ede1802b8e92d80544fc5b942220dc621874896a853e5f0a6ae6b8df6a25', '35714fd511b6064908da4ed77c12f587-79c2f3c3-2036-4f3e-9db2-efd52118c06c-0d981a4d', 'NIDTMAKBXLEVLIQBIOZSQUAYHD2OQDEZ33MXNHKOMDZ6DDALUP3LFSGVOJMJGY6D', True)
>>> sv.close()
>>> sv = SocialvoidClient()
>>> sv.session.public_hash, sv.session.private_hash, sv.session.session_id, sv.session.session_challenge, sv.session.session_exists = ('5ee8486fa6a9c7d4bdd234efdfa9099ae2ef5ab0d9aff77c004caf22d11e9c77', '1746ede1802b8e92d80544fc5b942220dc621874896a853e5f0a6ae6b8df6a25', '35714fd511b6064908da4ed77c12f587-79c2f3c3-2036-4f3e-9db2-efd52118c06c-0d981a4d', 'NIDTMAKBXLEVLIQBIOZSQUAYHD2OQDEZ33MXNHKOMDZ6DDALUP3LFSGVOJMJGY6D', True)
>>> sv.session.get()
Session(id='35714fd511b6064908da4ed77c12f587-79c2f3c3-2036-4f3e-9db2-efd52118c06c-0d981a4d', flags=[], authenticated=False, created=datetime.datetime(2021, 10, 6, 20, 13, 28), expires=datetime.datetime(2021, 10, 6, 20, 23, 28))
```
