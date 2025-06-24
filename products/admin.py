from django.contrib import admin
from .models import productsInfo
from .models import BikesDetails
from .models import BikeImage
from .models import batterie
from .models import batterie_image

# Register your models here.

class BikeImageInline(admin.TabularInline):
    model = BikeImage
    extra = 10
class BikesDetailAdmin(admin.ModelAdmin):
    inlines = [BikeImageInline]


admin.site.register(productsInfo)
admin.site.register(BikesDetails, BikesDetailAdmin)
admin.site.register(BikeImage)
admin.site.register(batterie)
admin.site.register(batterie_image)



