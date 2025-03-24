from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100)
    description = models.TextField()
    request_date = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    resolved_date = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(upload_to='service_requests/', null=True, blank=True)

    def __str__(self):
        return f"Request by {self.customer.name} on {self.request_date}"
