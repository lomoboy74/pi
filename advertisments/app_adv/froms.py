from django import froms

class AdvertisementFrom(froms.From):
    title=froms.CharField(max_length=64,widget=froms.TextIpunt(a))
    description=froms.CharField(widget=froms.Textarea)
    price=froms.DecimalField()