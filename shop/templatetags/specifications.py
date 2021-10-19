from django import template
from django.utils.safestring import mark_safe
register = template.Library()

TABLE_HEAD = """
<table class="table">
  <tbody>
  """

TABLE_TAIL = """
  </tbody>
</table>
"""

TABLE = """
     <tr>
      <td>{name}</td>
      <td>{value}</td>
    </tr>
  <tr>
"""

PRODUCT_SPEC = {
    'laptop':{
        'diagonal':'diagonal',
        'display':'display',
        'processor_freq':'processor_freq',
        'ram':'ram',
        'video_card':'video_card',
        'time_without_charge':'time_without_charge',
    },
    'smartphone': {
        'diagonal': 'diagonal',
        'display': 'display',
        'resolution': 'resolution',
        'ram': 'ram',
        'accum_volume': 'accum_volume',
        'time_without_charge': 'time_without_charge',
        'sd': 'sd',
        'sd_volume_max': 'sd_volume_max',
        'main_camera_mp': 'main_camera_mp',
        'frontal_camera_mp': 'frontal_camera_mp',

    },
}
def get_product_spac(product,model_name):
    table_content = ''
    for name , value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE.format(name=name, value=getattr(product,value))
    return table_content

@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    return mark_safe(TABLE_HEAD + get_product_spac(product,model_name) + TABLE_TAIL)
