# iamheadless_publisher_admin_documents

App to render homepage item type in `iamheadless_publisher_admin` frontend.

## Installation

Requires `iamheadless_publisher_admin`
Requires `iamheadless_publisher_file_handling`

1. install package
2. add `iamheadless_publisher_admin_documents` to `INSTALLED_APPS` in `settings.py`
3. add viewsets to `IAMHEADLESS_PUBLISHER_ADMIN_VIEWSET_LIST` in `settings.py`
```
[
    'iamheadless_publisher_admin_documents.viewsets.DocumentCreateViewSet',
    'iamheadless_publisher_admin_documents.viewsets.DocumentDeleteViewSet',
    'iamheadless_publisher_admin_documents.viewsets.DocumentRetrieveUpdateViewSet',
]
```
