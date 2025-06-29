from django.contrib import admin
from .models import productsInfo
from .models import BikesDetails
from .models import BikeImage
from .models import batterie
from .models import batterie_image
from .models import trotinette_electrique

# Register your models here.

class BikeImageInline(admin.TabularInline):
    model = BikeImage
    extra = 10
class BikesDetailAdmin(admin.ModelAdmin):
    inlines = [BikeImageInline]

class batterieImageInline(admin.TabularInline):
    model = batterie_image
    extra = 10
class batterieDetailAdmin(admin.ModelAdmin):
    inlines = [batterieImageInline]


admin.site.register(productsInfo)
admin.site.register(BikesDetails, BikesDetailAdmin)
admin.site.register(BikeImage)
admin.site.register(batterie, batterieDetailAdmin)
admin.site.register(batterie_image)
admin.site.register(trotinette_electrique)




