# Asynchronous Client

!!! note
    A method that requires authentication implicitly requires a session since you need one to authenticate

## `AsyncSocialvoidClient`

::: socialvoidpy.AsyncSocialvoidClient
    :docstring:
    :members: close get_protocol_version

### `Session`

::: socialvoidpy.async_client.Session
    :docstring:
    :members: create get logout authenticate_user register

### `Help`

::: socialvoidpy.async_client.Help
    :docstring:
    :members: get_community_guidelines get_privacy_policy get_server_information get_terms_of_service

### `Network`

::: socialvoidpy.async_client.Network
    :docstring:
    :members: get_me

### `Account`

::: socialvoidpy.async_client.Account
    :docstring:
    :members: delete_profile_picture set_profile_picture clear_profile_biography clear_profile_location

### `Cloud`

::: socialvoidpy.async_client.Cloud
    :docstring:
    :members: get_document

### `CDN`

::: socialvoidpy.async_client.CDN
    :docstring:
    :members: stream upload
