# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput
from models import Property, Availability, Tenant
from django.forms.fields import FileField


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u"用户名",
        error_messages={'required': '请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"用户名",
            }
        ),
    )    
    password = forms.CharField(
        required=True,
        label=u"密码",
        error_messages={'required': u'请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"密码",
            }
        ),
    )  
    
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm, self).clean()
            
#修改密码
class ChangepwdForm(forms.Form):
    oldpassword = forms.CharField(
        required=True,
        label=u"原密码",
        error_messages={'required': u'请输入原密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"原密码",
            }
        ),
    ) 
    newpassword1 = forms.CharField(
        required=True,
        label=u"新密码",
        error_messages={'required': u'请输入新密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"新密码",
            }
        ),
    )
    newpassword2 = forms.CharField(
        required=True,
        label=u"确认密码",
        error_messages={'required': u'请再次输入新密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"确认密码",
            }
        ),
    )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"所有项都为必填项")
        elif self.cleaned_data['newpassword1'] <> self.cleaned_data['newpassword2']:
            raise forms.ValidationError(u"两次输入的新密码不一样")
        else:
            cleaned_data = super(ChangepwdForm, self).clean()
        return cleaned_data


class PropertyForm(forms.Form):
    class Meta:
        model = Property
        only = ['NameUnicode', 'Name', 'VacancyRatio', 'AvailabilityCount',
            'RentableBuildingArea', 'GradeCode',
            'StreetNameUnicode', 'StreetFrom', 'SubmarketCluster',
            'YearBuilt', 
            'Latitude', 'Longitude', 'Type',  'EfficiencyPercent', 
            'StoryCount', 'TypicalFloorSize',
            'YearRenovated', 'CeilingHeightRange', 'DriverIns', 'ParkingRatio', 
            'LandArea', 'PropertyTypeName', 'BuildingTypeName', 'MetroLinkage',
            'Positioning', 'AreaRetail']
            
    _field_order = ['NameUnicode', 'Name', 'VacancyRatio', 'AvailabilityCount',
            'RentableBuildingArea', 'GradeCode',
            'StreetNameUnicode', 'StreetFrom', 'SubmarketCluster',
            'YearBuilt', 
            'Latitude', 'Longitude', 'Type',  'EfficiencyPercent', 
            'StoryCount', 'TypicalFloorSize',
            'YearRenovated', 'CeilingHeightRange', 'DriverIns', 'ParkingRatio', 
            'LandArea', 'PropertyTypeName', 'BuildingTypeName', 'MetroLinkage',
            'Positioning', 'AreaRetail', 'Photo', 'PDF']
    
    Image = FileField(u'上传载体图片',validators=[
        FileAllowed(['jpg', 'png', 'gif'], 'Images only!')
    ])
    Document = FileField(u'上传载体资料文档',validators=[
        FileAllowed(['pdf'], 'PDFs only!')
    ])
    
    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        field_order = getattr(self, '_field_order')
        visited = []
        if field_order:
            new_fields = OrderedDict()
            for field_name in field_order:
                if field_name in self._fields:
                    new_fields[field_name] = self._fields[field_name]
                    visited.append(field_name)
            for field_name in self._fields:
                if field_name in visited:
                    continue
                new_fields[field_name] = self._fields[field_name]
            self._fields = new_fields  
        

class AvailabilityForm(ModelForm):
    class Meta:
        model = Availability
        only = ['Floor', 'Unit', 'Status', 'Deco', 'LeaseAvailability', 'Area',
                'Eff', 'UnitPrice', 'UnitRental', 'ManagementFee']



class TenantForm(ModelForm):
    class Meta:
        model = Tenant
        only = ['TenantName', 'TenantType', 'TenantStatus', 'TenantProperty', 'TenantStartDate1', 'TenantStartDate2', 'TenantStock','PhoneNumber',
                'ContactorName', 'ContactorPhone', 'ContactorPosition', 'Description']