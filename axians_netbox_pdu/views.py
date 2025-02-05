from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from netbox.views.generic import BulkDeleteView, BulkImportView, ObjectEditView, ObjectListView

from .filters import PDUConfigFilter
from .forms import PDUConfigCSVForm, PDUConfigFilterForm, PDUConfigForm
from .models import PDUConfig
from .tables import PDUConfigBulkTable, PDUConfigTable

from django.conf import settings
from packaging import version

NETBOX_CURRENT_VERSION = version.parse(settings.VERSION)

class PDUConfigListView(PermissionRequiredMixin, ObjectListView):
    """View for listing all PDUConfig items"""

    permission_required = "axians_netbox_pdu.view_pduconfig"
    queryset = PDUConfig.objects.all()
    filterset = PDUConfigFilter
    filterset_form = PDUConfigFilterForm
    table = PDUConfigTable
    if NETBOX_CURRENT_VERSION >= version.parse("3.0"):
        template_name = "axians_netbox_pdu/pduconfig_list_3_x.html"
    else:
        template_name = "axians_netbox_pdu/pduconfig_list.html"


class PDUConfigCreateView(PermissionRequiredMixin, ObjectEditView):
    """View for creating a new PDUConfig"""

    permission_required = "axians_netbox_pdu.add_pduconfig"
    model = PDUConfig
    queryset = PDUConfig.objects.all()
    model_form = PDUConfigForm
    if NETBOX_CURRENT_VERSION >= version.parse("3.0"):
        template_name = "axians_netbox_pdu/pduconfig_edit_3_x.html"
    else:
        template_name = "axians_netbox_pdu/pduconfig_edit.html"
    default_return_url = "plugins:axians_netbox_pdu:pduconfig_list"


class PDUConfigImportView(PermissionRequiredMixin, BulkImportView):
    """View for bulk-importing a CSV file to create PDUConfigs"""

    permission_required = "axians_netbox_pdu.add_pduconfig"
    queryset = PDUConfig.objects.all()
    model_form = PDUConfigCSVForm
    table = PDUConfigBulkTable
    default_return_url = "plugins:axians_netbox_pdu:pduconfig_list"


class PDUConfigBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    """View for deleting one or more PDUConfigs."""

    permission_required = "axians_netbox_pdu.delete_pduconfig"
    queryset = PDUConfig.objects.filter()
    table = PDUConfigTable
    default_return_url = "plugins:axians_netbox_pdu:pduconfig_list"


class PDUConfigEditView(PDUConfigCreateView):
    permission_required = "axians_netbox_pdu.change_pduconfig"
