from django.db import models
from django.utils import timezone
from datetime import date as pydate


# Site-related tables
# -------------------------
class Customers(models.Model):
    first_name = models.CharField(max_length=90)
    second_name = models.CharField(max_length=120)
    surname = models.CharField(max_length=130)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    account_create_date = models.DateField(default=pydate.today)
    timezone = models.ForeignKey(
        'Timezones',
        on_delete=models.CASCADE
    )


# ToDo: add timezones from pytz.common_timezones
class Timezones(models.Model):
    tz_name = models.CharField(max_length=40)
    tz_utc_name = models.CharField(max_length=3)


# Product-related tables
# -------------------------
class Manufacturer(models.Model):
    man_name = models.CharField(max_length=80)
    description = models.TextField()
    contacts = models.CharField(max_length=100)


class Product(models.Model):
    """Is abstract class. Added for flexibility.
    With this class can easily be added new categories:
    accessories, modules, etc.
    There are fields, common for every category
    of products.
    """
    full_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=30)
    manufacturer_id = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE
    )
    discontinued = models.BooleanField(default=False)
    description = models.TextField()

    class Meta:
        ordering = ["short_name"]


class Prices(models.Model):
    product_id = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["price_date"]


# SBC specifications-related tables
# -------------------------
class Cpu_platforms(models.Model):
    """Corresponds to cpu_platform.
    arm, x86, other
    """
    cpu_platform_name = models.CharField(max_length=10)


class Cpu(models.Model):
    # Full name of cpu to display in filters
    # Example:
    # Broadcom BCM2711B0 quad-core A72(ARMv8-A) 64-bit
    name = models.CharField(max_length=100)
    platform = models.ForeignKey(
        'Cpu_platforms',
        on_delete=models.CASCADE
    )
    # Cannot be negative or zero
    core_amount = models.SmallIntegerField()
    is_64_bit = models.BooleanField(default=False)
    # Represents frequency in mhz
    frequency = models.IntegerField()


class Sbc_types(models.Model):
    # SOM/COM/module
    # SBC
    # Carrier board
    type_name = models.CharField(max_length=15)


class Ram_types(models.Model):
    """Represents standard of ram"""
    # DDR4, LPDDR3, etc.
    ram_type_name = models.CharField(max_length=25)


class Sbc(Product):
    sbc_name = models.CharField(max_length=70)
    product_id = models.ForeignKey(
        'Product',
        related_name='product',
        on_delete=models.CASCADE
    )
    sbc_type_id = models.ForeignKey(
        'Sbc_types',
        on_delete=models.CASCADE
    )
    cpu_id = models.ForeignKey(
        'Cpu',
        on_delete=models.CASCADE
    )
    gpu_id = models.ForeignKey(
        'Gpu',
        on_delete=models.CASCADE
    )
    mcu_id = models.ForeignKey(
        'Mcu',
        on_delete=models.CASCADE
    )
    npu_id = models.ForeignKey(
        'Npu',
        on_delete=models.CASCADE
    )
    fpga_id = models.ForeignKey(
        'Fpga',
        on_delete=models.CASCADE
    )
    ram_type_id = models.ForeignKey(
        'Ram_types',
        on_delete=models.CASCADE
    )
    storage_type_id = models.ForeignKey(
        'Sbc_storage_types',
        on_delete=models.CASCADE
    )
    storage_amount = models.SmallIntegerField()
    wifi_standard_id = models.ForeignKey(
        'Wifi_standards',
        on_delete=models.CASCADE
    )
    bl_standard_id = models.ForeignKey(
        'Bluetooth',
        on_delete=models.CASCADE
    )
    bl_low_energy = models.BooleanField(default=False)
    ethernet_speed_id = models.ForeignKey(
        'Ethernet_speeds',
        on_delete=models.CASCADE
    )
    ethernet_port_amount = models.SmallIntegerField()
    gpio_pins = models.SmallIntegerField()


class Wifi_standards(models.Model):
    wifi_standard_name = models.CharField(max_length=40)


class Bluetooth(models.Model):
    """Stores version of Bluetooth"""
    # Examples: 5.0, 4.2, 2.1
    bluetooth_version = models.CharField(max_length=3)


class Sbc_storage_types(models.Model):
    storage_type_name = models.CharField(max_length=15)


class Storage_expansions(models.Model):
    # Examples: 'm.2 nvme', 'sata', 'micro sd'
    storage_expansion_name = models.CharField(max_length=25)
    # Represents capacity in GBytes
    max_capacity = models.DecimalField(max_digits=5, decimal_places=2)


class Sbc_storage_expansions(models.Model):
    """Resolves many-to-many relationship
    between Storage_expansions and Sbc"""
    sbc_id = models.ForeignKey(
        'Sbc',
        on_delete=models.CASCADE
    )
    st_exp_id = models.ForeignKey(
        'Storage_expansions',
        on_delete=models.CASCADE
    )


class Os_families(models.Model):
    family_name = models.CharField(max_length=25)


class Os(models.Model):
    os_name = models.CharField(max_length=50)
    os_family_id = models.ForeignKey(
        'Os_families',
        on_delete=models.CASCADE
    )


class Supported_os(models.Model):
    """Resolves many-to-many relationship
    between Sbc and Os"""
    sbc_id = models.ForeignKey(
        'Sbc',
        on_delete=models.CASCADE
    )
    os_id = models.ForeignKey(
        'Os',
        on_delete=models.CASCADE
    )


class Ethernet_speeds(models.Model):
    # Has only three values:
    # 10 = 10 Mbps;
    # 100 = 100 Mbps;
    # 1000 = 1 Gbps
    ethernet_speed = models.SmallIntegerField(default=100)


class Npu(models.Model):
    npu_name = models.CharField(max_length=45)


class Mcu(models.Model):
    mcu_name = models.CharField(max_length=45)


class Fpga(models.Model):
    fpga_name = models.CharField(max_length=45)


class Port_names(models.Model):
    port_name = models.CharField(max_length=40)


class Available_ports(models.Model):
    """Resolves many-to-many relationship
    between Port_names and Sbc"""
    sbc_id = models.ForeignKey(
        'Sbc',
        on_delete=models.CASCADE
    )
    port_name_id = models.ForeignKey(
        'Port_names',
        on_delete=models.CASCADE
    )
    # Is present, if amount of ports > 1
    amount = models.SmallIntegerField(default=1)


class Gpu_family(models.Model):
    gpu_family_name = models.CharField(max_length=50)


class Gpu(models.Model):
    name = models.CharField(max_length=100)
    gpu_family = models.ForeignKey(
        'Gpu_family',
        on_delete=models.CASCADE
    )
    frequency = models.IntegerField()


class Graphics_api(models.Model):
    graph_api_name = models.CharField(max_length=50)


class Supported_graph_api(models.Model):
    gpu_id = models.ForeignKey(
        'Gpu',
        on_delete=models.CASCADE
    )
    graph_api_id = models.ForeignKey(
        'Graphics_api',
        on_delete=models.CASCADE
    )
    graph_api_version = models.CharField(max_length=40)
