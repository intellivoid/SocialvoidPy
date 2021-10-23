# Synchronous Client

## `SocialvoidClient`

::: socialvoidpy.SocialvoidClient
    :docstring:
    :members: close get_protocol_version

### `Session`

::: socialvoidpy.sync_client.Session
    :docstring:
    :members: create get logout authenticate_user register

### `Help`

::: socialvoidpy.sync_client.Help
    :docstring:
    :members: get_community_guidelines get_privacy_policy get_server_information get_terms_of_service

### `Network`

::: socialvoidpy.sync_client.Network
    :docstring:
    :members: get_me get_peer get_profile follow_peer unfollow_peer get_followers get_following iter_followers iter_following

### `Account`

::: socialvoidpy.sync_client.Account
    :docstring:
    :members: delete_profile_picture set_profile_picture clear_profile_biography clear_profile_location clear_profile_url update_profile_biography update_profile_location update_profile_name update_profile_url

### `Cloud`

::: socialvoidpy.sync_client.Cloud
    :docstring:
    :members: get_document

### `CDN`

::: socialvoidpy.sync_client.CDN
    :docstring:
    :members: stream upload

### `Timeline`

::: socialvoidpy.sync_client.Timeline
    :docstring:
    :members: compose get_post delete like get_feed get_likers get_reposters get_quotes get_replies iter_feed iter_likers iter_reposters iter_quotes iter_replies
