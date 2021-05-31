from django.db import models


class ThinCodeName(models.Model):
    NAME_CHOICES = (
        ('إدارة المشاة', 'إدارة المشاة'),
        ('إدارة المدرعات', 'إدارة المدرعات'),
        ('إدارة المدفعية', 'إدارة المدفعية'),
        ('إدارة المركبات', 'إدارة المركبات'),
        ('إدارة الشرطة العسكرية', 'إدارة الشرطة العسكرية'),
        ('إدارة الشؤون المعنوية', 'إدارة الشؤون المعنوية'),
        ('جهاز الرياضة العسكري', 'جهاز الرياضة العسكري'),
        ('هيئة التدريب للقوات المسلحة', 'هيئة التدريب للقوات المسلحة'),
        ('هيئة التفتيش للقوات المسلحة', 'هيئة التفتيش للقوات المسلحة'),
        ('إدارة الأسلحة والذخيرة', 'إدارة الأسلحة والذخيرة'),
        ('إدارة البحوث الفنية والتطوير', 'إدارة البحوث الفنية والتطوير'),
        ('مركز التنمية البشرية والعلوم السلوكية', 'مركز التنمية البشرية والعلوم السلوكية'),
        ('إدارة نوادي وفاندق ضباط ق.م', 'إدارة نوادي وفاندق ضباط ق.م'),
        (' جهاز مشروعات الخدمة الوطنية', 'جهاز مشروعات الخدمة الوطنية'),
        ('هيئة القضاء العسكري', 'هيئة القضاء العسكري'),
        ('إدارة المدعي العام', 'إدارة المدعي العام'),
        ('إدارة المحاكم العسكرية', 'إدارة المحاكم العسكرية'),
        ('إدارة الحرب الكيمائية', 'إدارة الحرب الكيمائية'),
        ('إدارة المتاحف العسكرية', 'إدارة المتاحف العسكرية'),
        ('قيادة قوات حرس الحدود', 'قيادة قوات حرس الحدود'),
        ('قيادة قوات الدفاع الشعبي والعسكري', 'قيادة قوات الدفاع الشعبي والعسكري'),
        ('إدارة الموسيقات العسكرية', 'إدارة الموسيقات العسكرية'),
        ('دار المحفوظات المركزية', 'دار المحفوظات المركزية'),
        ('المركز الرئيسية للتنبؤات الجوية', 'المركز الرئيسية للتنبؤات الجوية'),
        ('جهاز مراقبة وضمان الجودة/هيئة التسليح ق.م', 'جهاز مراقبة وضمان الجودة/هيئة التسليح ق.م'),
        (' إدارة التعليم والتدريب المهني', 'إدارة التعليم والتدريب المهني'),
        ('قيادة القوات الجوية', 'قيادة القوات الجوية'),
        ('المركز الإعلامي العسكري', 'المركز الإعلامي العسكري'),
        ('مركز تطوير وصيانة معدات النظم الألية', 'مركز تطوير وصيانة معدات النظم الألية'),
        ('مركز تدريب الية القيادة والسيطرة', 'مركز تدريب الية القيادة والسيطرة'),
        ('المنظومة تحرير', 'المنظومة تحرير'),
        ('إدارة المحفوظات المركزية', 'إدارة المحفوظات المركزية'),
        ('إدارة المياه', 'إدارة المياه'),
        ('إدارة الإشارة', 'إدارة الإشارة'),
        ('CCTV ', 'CCTV'),
        ('دفاع جوي', 'دفاع جوي'),
        ('جهاز تنمية الموارد المالية', 'جهاز تنمية الموارد المالية'),
        ('مؤسسة صندوق الجلاء للقوات المسلحة', 'مؤسسة صندوق الجلاء للقوات المسلحة'),
        ('صندوق التأميني التكميلي', 'صندوق التأميني التكميلي'),
        ('مؤسسة القروض', 'مؤسسة القروض'),
        ('صندوق التأمين الخاص', 'صندوق التأمين الخاص'),
        ('صندوق إسكان أفراد القوات المسلحة', 'صندوق إسكان أفراد القوات المسلحة'),
        ('هيئة الشؤون المالية للقوات المسلحة', 'هيئة الشؤون المالية للقوات المسلحة'),
        ('إدارة التفتيش والمحاسبات', 'إدارة التفتيش والمحاسبات'),
        ('إدارة الميزانية', 'إدارة الميزانية'),
        ('إدارة العلاقات العامة والتمويل الخارجي', 'إدارة العلاقات العامة والتمويل الخارجي'),
        ('الإدارة المركزية للمحاسبات', 'الإدارة المركزية للمحاسبات'),
        ('إدارة التأمين والمعاشات', 'إدارة التأمين والمعاشات'),
        ('هيئة التنظيم والإدارة للقوات المسلحة', 'هيئة التنظيم والإدارة للقوات المسلحة'),
        ('إدارة التجنيد والتعبئة', 'إدارة التجنيد والتعبئة'),
        ('إدارة السجلات العسكرية', 'إدارة السجلات العسكرية'),
        ('فرع الإنتقاء والتوجيه', 'فرع الإنتقاء والتوجي'),
        ('إدارة شؤون العاملين المدنيين', 'إدارة شؤون العاملين المدنيين'),

    )
    name = models.CharField(max_length=255, null=True, blank=True, choices=NAME_CHOICES, unique=True)
    code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class ThinCodePlace(models.Model):
    code = models.ForeignKey(ThinCodeName, on_delete=models.CASCADE)
    place = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        self.code.name


class ThinCodeTotal(models.Model):
    code = models.ForeignKey(ThinCodeName, on_delete=models.CASCADE)
    total = models.IntegerField(null=True, blank=True)

    def __str__(self):
        self.code.name


class ThinUnits(models.Model):
    STATUS_CHOICES = (
        ('مخزن', 'مخزن'),
        ('جارى العمل', 'جارى العمل'),
        ('انتهى العمل', 'انتهى العمل')
    )

    status = models.CharField(max_length=255, blank=True, choices=STATUS_CHOICES, null=True)
    total = models.ForeignKey(ThinCodeTotal, on_delete=models.CASCADE, null=True)
    place = models.ForeignKey(ThinCodePlace, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.status


class ThinDevicesUnits(models.Model):
    code = models.ForeignKey(ThinCodeName, on_delete=models.CASCADE, null=True)
    total_devices = models.ForeignKey(ThinCodeTotal, on_delete=models.CASCADE, null=True)
    devices_done = models.IntegerField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    short_name = models.CharField(max_length=255, null=True, blank=True)
    epg = models.CharField(max_length=255, null=True, blank=True)
    cdb = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    database_zone = models.CharField(max_length=255, null=True, blank=True)
    database_name = models.CharField(max_length=255, null=True, blank=True)
    catoperation = models.CharField(max_length=255, null=True, blank=True)
    mangloc = models.CharField(max_length=255, null=True, blank=True)
    seprated_thin = models.CharField(max_length=255, null=True, blank=True)
    center110 = models.CharField(max_length=255, null=True, blank=True)
    center100 = models.CharField(max_length=255, null=True, blank=True)
    recieved_date = models.DateField(null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    build = models.ForeignKey(ThinCodePlace, on_delete=models.CASCADE, null=True)
    groupwork = models.CharField(max_length=255, null=True, blank=True)

    @property
    def remain_devices(self):
        if self.devices_done is None:
            return self.total_devices.total
        else:
            return self.total_devices.total - self.devices_done


    @property
    def per25(self):
        if self.devices_done is None:
            return self.remain_devices
        else:
            return self.remain_devices * 25 / 100

    @property
    def per50(self):
        if self.devices_done is None:
            return self.remain_devices
        else:
            return self.remain_devices * 50 / 100

    def __str__(self):
        return self.category
