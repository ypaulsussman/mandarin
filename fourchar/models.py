from django.db import models


class Chengyu(models.Model):
    RARITY_CHOICES = [
        {1, 'Very Common'},
        {2, 'Common'},
        {3, 'Uncommon'},
        {4, 'Rare'},
        {5, 'Very Rare'}
    ]
    z_rarity = models.IntegerField(
        choices=RARITY_CHOICES,
        default=3)
    demo_sentence_zh = models.TextField()
    demo_sentence_pn = models.TextField()
    demo_sentence_en = models.TextField()
    chengyu_text = models.CharField(max_length=250)
    chengyu_translation = models.CharField(max_length=500)
    def __str__(self):
        return self.chengyu_text
