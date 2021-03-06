# Generated by Django 3.2 on 2021-05-30 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ThinCodeName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('إدارة المشاة', 'إدارة المشاة'), ('إدارة المدرعات', 'إدارة المدرعات'), ('إدارة المدفعية', 'إدارة المدفعية'), ('إدارة المركبات', 'إدارة المركبات'), ('إدارة الشرطة العسكرية', 'إدارة الشرطة العسكرية'), ('إدارة الشؤون المعنوية', 'إدارة الشؤون المعنوية'), ('جهاز الرياضة العسكري', 'جهاز الرياضة العسكري'), ('هيئة التدريب للقوات المسلحة', 'هيئة التدريب للقوات المسلحة'), ('هيئة التفتيش للقوات المسلحة', 'هيئة التفتيش للقوات المسلحة'), ('إدارة الأسلحة والذخيرة', 'إدارة الأسلحة والذخيرة'), ('إدارة البحوث الفنية والتطوير', 'إدارة البحوث الفنية والتطوير'), ('مركز التنمية البشرية والعلوم السلوكية', 'مركز التنمية البشرية والعلوم السلوكية'), ('إدارة نوادي وفاندق ضباط ق.م', 'إدارة نوادي وفاندق ضباط ق.م'), (' جهاز مشروعات الخدمة الوطنية', 'جهاز مشروعات الخدمة الوطنية'), ('هيئة القضاء العسكري', 'هيئة القضاء العسكري'), ('إدارة المدعي العام', 'إدارة المدعي العام'), ('إدارة المحاكم العسكرية', 'إدارة المحاكم العسكرية'), ('إدارة الحرب الكيمائية', 'إدارة الحرب الكيمائية'), ('إدارة المتاحف العسكرية', 'إدارة المتاحف العسكرية'), ('قيادة قوات حرس الحدود', 'قيادة قوات حرس الحدود'), ('قيادة قوات الدفاع الشعبي والعسكري', 'قيادة قوات الدفاع الشعبي والعسكري'), ('إدارة الموسيقات العسكرية', 'إدارة الموسيقات العسكرية'), ('دار المحفوظات المركزية', 'دار المحفوظات المركزية'), ('المركز الرئيسية للتنبؤات الجوية', 'المركز الرئيسية للتنبؤات الجوية'), ('جهاز مراقبة وضمان الجودة/هيئة التسليح ق.م', 'جهاز مراقبة وضمان الجودة/هيئة التسليح ق.م'), (' إدارة التعليم والتدريب المهني', 'إدارة التعليم والتدريب المهني'), ('قيادة القوات الجوية', 'قيادة القوات الجوية'), ('المركز الإعلامي العسكري', 'المركز الإعلامي العسكري'), ('مركز تطوير وصيانة معدات النظم الألية', 'مركز تطوير وصيانة معدات النظم الألية'), ('مركز تدريب الية القيادة والسيطرة', 'مركز تدريب الية القيادة والسيطرة'), ('المنظومة تحرير', 'المنظومة تحرير'), ('إدارة المحفوظات المركزية', 'إدارة المحفوظات المركزية'), ('إدارة المياه', 'إدارة المياه'), ('إدارة الإشارة', 'إدارة الإشارة'), ('CCTV ', 'CCTV'), ('دفاع جوي', 'دفاع جوي'), ('جهاز تنمية الموارد المالية', 'جهاز تنمية الموارد المالية'), ('مؤسسة صندوق الجلاء للقوات المسلحة', 'مؤسسة صندوق الجلاء للقوات المسلحة'), ('صندوق التأميني التكميلي', 'صندوق التأميني التكميلي'), ('مؤسسة القروض', 'مؤسسة القروض'), ('صندوق التأمين الخاص', 'صندوق التأمين الخاص'), ('صندوق إسكان أفراد القوات المسلحة', 'صندوق إسكان أفراد القوات المسلحة'), ('هيئة الشؤون المالية للقوات المسلحة', 'هيئة الشؤون المالية للقوات المسلحة'), ('إدارة التفتيش والمحاسبات', 'إدارة التفتيش والمحاسبات'), ('إدارة الميزانية', 'إدارة الميزانية'), ('إدارة العلاقات العامة والتمويل الخارجي', 'إدارة العلاقات العامة والتمويل الخارجي'), ('الإدارة المركزية للمحاسبات', 'الإدارة المركزية للمحاسبات'), ('إدارة التأمين والمعاشات', 'إدارة التأمين والمعاشات'), ('هيئة التنظيم والإدارة للقوات المسلحة', 'هيئة التنظيم والإدارة للقوات المسلحة'), ('إدارة التجنيد والتعبئة', 'إدارة التجنيد والتعبئة'), ('إدارة السجلات العسكرية', 'إدارة السجلات العسكرية'), ('فرع الإنتقاء والتوجيه', 'فرع الإنتقاء والتوجي'), ('إدارة شؤون العاملين المدنيين', 'إدارة شؤون العاملين المدنيين')], max_length=255, null=True, unique=True)),
                ('code', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ThinCodePlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.thincodename')),
            ],
        ),
        migrations.CreateModel(
            name='ThinCodeTotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(blank=True, null=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.thincodename')),
            ],
        ),
        migrations.CreateModel(
            name='ThinUnits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('مخزن', 'مخزن'), ('جارى العمل', 'جارى العمل'), ('انتهى العمل', 'انتهى العمل')], max_length=255, null=True)),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='devices.thincodeplace')),
                ('total', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='devices.thincodetotal')),
            ],
        ),
        migrations.CreateModel(
            name='ThinDevicesUnits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devices_done', models.IntegerField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('short_name', models.CharField(blank=True, max_length=255, null=True)),
                ('epg', models.CharField(blank=True, max_length=255, null=True)),
                ('cdb', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('database_zone', models.CharField(blank=True, max_length=255, null=True)),
                ('database_name', models.CharField(blank=True, max_length=255, null=True)),
                ('catoperation', models.CharField(blank=True, max_length=255, null=True)),
                ('mangloc', models.CharField(blank=True, max_length=255, null=True)),
                ('seprated_thin', models.CharField(blank=True, max_length=255, null=True)),
                ('center110', models.CharField(blank=True, max_length=255, null=True)),
                ('center100', models.CharField(blank=True, max_length=255, null=True)),
                ('recieved_date', models.DateField(blank=True, null=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('groupwork', models.CharField(blank=True, max_length=255, null=True)),
                ('build', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='devices.thincodeplace')),
                ('code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='devices.thincodename')),
                ('total_devices', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='devices.thincodetotal')),
            ],
        ),
    ]
