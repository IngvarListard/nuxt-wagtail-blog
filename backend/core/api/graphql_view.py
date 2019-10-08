"""Apply multipart request spec to django"""
from graphene_file_upload.django import FileUploadGraphQLView


class CustomGraphQLView(FileUploadGraphQLView):
    """Handles multipart/form-data content type in django views"""

    def __init__(self, *args, **kwargs):
        self.batch_status = kwargs.get('batch', False)
        super(CustomGraphQLView, self).__init__(*args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        """Отключение батчинга в случае загрузки файлов"""
        file_uploading = bool(request.FILES)
        if file_uploading:
            # если что-то пойдёт не так можно добавить батч из настроек джанги
            self.batch_status = self.batch
            self.batch = False
        else:
            self.batch = self.batch_status
        response = super(CustomGraphQLView, self).dispatch(request, *args, **kwargs)
        self.batch = self.batch_status
        return response

