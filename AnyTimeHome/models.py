from django.db import models

# Create your models here.
class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30,primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    def __unicode__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'auth_user'

#reportplatform models
class UserInfo(models.Model):
    userid = models.BigIntegerField(db_column='UserID', primary_key=True) # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID', blank=True, null=True) # Field name made lowercase.
    departmentno = models.IntegerField(db_column='DepartmentNO', blank=True, null=True) # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50) # Field name made lowercase.
    useralias = models.CharField(db_column='UserAlias', unique=True, max_length=50) # Field name made lowercase.
    userrole = models.CharField(db_column='UserRole', max_length=1) # Field name made lowercase.
    userstatus = models.CharField(db_column='UserStatus', max_length=1) # Field name made lowercase.
    gmtcreate = models.DateTimeField(db_column='GmtCreate') # Field name made lowercase.
    gmtmodified = models.DateTimeField(db_column='GmtModified', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_info'

    def __unicode__(self):
        return self.username

class serverlist(models.Model):
    serverip=models.CharField(primary_key=True,max_length=50)
    serverenv=models.CharField(max_length=50)

    def __unicode__(self):
        return self.serverip

class natlog(models.Model):
    ccman=models.ForeignKey(AuthUser)
    ccserver=models.ForeignKey(serverlist)
    ftime=models.DateTimeField()
    btime=models.DateTimeField()
    cctime=models.DateTimeField()