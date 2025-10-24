from django.db import models

class FeeStructure(models.Model):
    student_class = models.ForeignKey("Class", on_delete=models.CASCADE)  
    stream = models.ForeignKey("Stream", on_delete=models.CASCADE, null=True, blank=True)  

    admission_fee = models.DecimalField(max_digits=10, decimal_places=2)
    rcf = models.DecimalField(max_digits=10, decimal_places=2)  
    cwf = models.DecimalField(max_digits=10, decimal_places=2)   
    ccwf = models.DecimalField(max_digits=10, decimal_places=2)  

    def total_fee(self):
        return self.admission_fee + self.rcf + self.cwf + self.ccwf

    def __str__(self):
        if self.stream:
            return f"Fee Structure for {self.student_class} ({self.stream})"
        return f"Fee Structure for {self.student_class}"