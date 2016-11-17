# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# models.py
class Property(models.Model):
    __tablename__ = 'property'
    ImageId = models.CharField(max_length=255)
    DocumentId = models.CharField(max_length=255)
    #Name = models.CharField(models.NVARCHAR(255), '名称(EN)')
    NameUnicode = models.CharField('载体名称', max_length=255, unique=True, null=False) 
    GradeCode = models.CharField( '级别定位', max_length=10, default="") 
    #SubmarketId = models.CharField(models.Integer)
    #MarketId = models.CharField(models.Integer)
    #ParentMarketId = models.CharField(models.Integer)
    #StreetId = models.CharField(models.Integer)
    #StreetName = models.CharField(models.NVARCHAR(255), default="", '街道(EN)')
    StreetNameUnicode = models.CharField('街道(CN)',max_length=255, default="")
    StreetFrom = models.CharField('门牌号', max_length=255)
    #StreetTo = models.CharField(models.Integer, default=0)
    #RegionId = models.CharField(models.Integer)
    #RegionName = models.CharField(models.NVARCHAR(255), default="", '国家(EN)')
    #RegionNameUnicode = models.CharField(models.NVARCHAR(255), default="", '国家(CN)')
    #CityId = models.CharField(models.Integer)
    #CityName = models.CharField(models.NVARCHAR(255), default="", '城市(EN)')
    #CityNameUnicode = models.CharField(models.NVARCHAR(255), default="", '城市(CN)')
    #CountryISOICode = models.CharField(models.Integer)
    #CountryISOCode = models.CharField(models.NVARCHAR(255))
    #CountryISO3Code = models.CharField(models.NVARCHAR(255))
    #CountryName = models.CharField(models.NVARCHAR(255), default="", '国家(EN)')
    YearBuilt = models.CharField('完工时间', max_length=255, default="")
    #HasStrataTitle = models.CharField(models.NVARCHAR(255))
    Latitude = models.DecimalField('纬度', max_digits=12, decimal_places=9)
    Longitude = models.DecimalField('经度', max_digits=12, decimal_places=9)
    #StatusCode = models.CharField(models.NVARCHAR(255))
    #TypeId = models.CharField(models.Integer)
    Type = models.CharField('类型', max_length=255, default="")
    VacancyRatio = models.CharField('空置率', max_length=255)
    EfficiencyPercent = models.CharField('得房率', max_length=255)
    AvailabilityCount = models.IntegerField('可租赁单元数量', max_length=255)
    UpdateDate = models.DateField('更新时间', auto_now=True)
    StoryCount = models.CharField('总楼层', max_length=255)
    RentableBuildingArea = models.CharField('可租赁总面积', max_length=255)
    TypicalFloorSize = models.CharField('标准楼层面积', max_length=255)
    YearRenovated = models.CharField('重装修日期', max_length=255, default="")
    #CleanZip = models.CharField(models.Integer)
    #CleanCity = models.CharField(models.NVARCHAR(255), default="")
    SubmarketCluster = models.CharField('所属分中心区域', max_length=255)
    CeilingHeightRange = models.CharField('层高范围', max_length=255,  )
    CarParking = models.CharField('车位数', max_length=255,  )
    ParkingRatio = models.CharField('车位比', max_length=255)
    LandArea = models.CharField('占地面积', max_length=255)
    AddressLine1 = models.CharField('地址', max_length=255)
    PropertyTypeName = models.CharField('载体类型', max_length=255, default="")
    #PropertyTypeCode = models.CharField(models.Integer)
    BuildingTypeName = models.CharField('建筑类型', max_length=255,  default="")
    #BuildingSubTypeName = models.CharField(models.NVARCHAR(255), default="")
    MetroLinkage = models.CharField('地铁信息', max_length=255, default="")
    Positioning = models.CharField('载体档次定位', max_length=255, default="")
    #AreaRetail = models.CharField(models.Integer, '零售业可租赁面积')
    #SubmarketClusterId = models.CharField(models.Integer)
    #CustomClusterId = models.CharField(models.Integer)
    #MetroStatisticalAreaId = models.CharField(models.Integer)
    #MetroDivisionId = models.CharField(models.Integer)
    #MicroMarketId = models.CharField(models.Integer)
    
    def __unicode__(self): 
        return self.name
    
class Availability(models.Model):
    __tablename__ = 'availability'
    Property = models.ForeignKey(Property, verbose_name='所属载体')
    #LegancyBuildingId = models.CharField(models.Integer)
    #SubmarketId = models.CharField(models.Integer)
    #MarketId = models.CharField(models.Integer)
    #ParentMarketId = models.CharField(models.Integer)
    Floor = models.CharField('楼层', max_length=255) #
    Unit = models.CharField('单元区域', max_length=255) #
    #StatusId = models.CharField(models.Integer)
    Status = models.CharField('状态', max_length=255) #
    Deco = models.CharField('装修', max_length=255)
    #LeaseAvailabilityId = models.CharField(models.Integer)
    LeaseAvailability = models.DateField('可租日期', auto_now=False, auto_now_add=False)
    Area = models.CharField('可租赁面积', max_length=255) #
    #AreaType = models.CharField(models.NVARCHAR(255))
    Eff = models.CharField('得房率', max_length=255)
    UnitPrice = models.CharField('出售单价', max_length=255)
    UnitRental = models.CharField('租赁单价', max_length=255)
    #UnitRentalType = models.CharField(models.NVARCHAR(255))
    ManagementFee = models.CharField('物业管理费', max_length=255)
    UpdateDate = models.DateField('更新时间', auto_now=True)
    #StatusName = models.CharField(models.NVARCHAR(255))
    
    def __unicode__(self): 
        return self.name
    
class Tenant(models.Model):
    __tablename__ = 'tenant'
    Property = models.ForeignKey(Property, verbose_name='所属载体')
    TenantName = models.CharField('租户名称', max_length=255) 
    TenantType = models.CharField('租户分类', max_length=255) 
    TenantStatus = models.CharField('租户状态', max_length=255)
    #TenantProperty = models.CharField(models.NVARCHAR(255),'租户载体')
    #TenantPropertyType = models.CharField(models.NVARCHAR(255),'租户载体类型')
    TenantStartDate = models.DateField('租赁起始时间', auto_now=False, auto_now_add=False)
    TenantEndDate = models.DateField('租赁到期时间', auto_now=False, auto_now_add=False)
    #TenantStock = models.CharField(models.NVARCHAR(255),'租户载体单元')
    PhoneNumber = models.CharField('联系电话', max_length=255)
    ContactorName = models.CharField('联系人姓名', max_length=255)
    #ContactorPhone = models.CharField(models.NVARCHAR(255),'联系人电话')
    ContactorPosition = models.CharField('联系人称谓', max_length=255)
    Description = models.CharField('备注', max_length=255)
    
    def __unicode__(self): 
        return self.name
