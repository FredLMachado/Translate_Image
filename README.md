# How to run

- Setup .env file with google api key.json path;
- Access Google Cloud to generate your key.json;
- `make install`;
- Print your screen or copy an image to clipboard for this usage example;
- `make run`;

# API key

- .env file should look like

```
GOOGLE_APPLICATION_CREDENTIALS=/path/to/api/key.json
```

- key.json should be generated from Google Cloud and will look like:

```json
{
    "type": "...",
    "project_id": "...",
    "private_key_id": "...",
    "private_key": "-----BEGIN PRIVATE KEY-----\n....\n-----END PRIVATE KEY-----\n",
    "client_email": "...",
    "client_id": "...",
    "auth_uri": "...",
    "token_uri": "...",
    "auth_provider_x509_cert_url": "...",
    "client_x509_cert_url": "...",
    "universe_domain": "..."
}
```

# Options

```bash
-f [file path, Leave empty to use clipboard Image]
-s [source language]
-t [target language]
```
