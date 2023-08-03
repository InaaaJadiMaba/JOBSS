from django.db import models

class user(models.Model):
    username = models.CharField(primary_key = True, max_length=50)
    password = models.CharField(max_length=20)
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama


class magang(models.Model):
    Judul = models.CharField(max_length=50)
    Jurusan = models.CharField(max_length=50)
    Deskripsi = models.TextField()
    Deadline = models.DateField()
    Publish = models.DateTimeField()
    Nama_id = models.ForeignKey(user, null=True, blank=True, on_delete=models.CASCADE)
    is_closed = models.BooleanField(default=True, null=None, blank=None)
    file = models.FileField(upload_to='file/', blank=True)

    def __str__(self):
        return self.Judul