from django.db import models 

class Author(models.Model): 
    author_id = models.AutoField(primary_key=True) 
    author_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.author_id}: {self.author_name}'
    
    class Meta: 
        db_table = "Authors"


class Journal(models.Model): 
    journal_id = models.AutoField(primary_key=True)
    journal_name = models.CharField(max_length=50)

    class Meta: 
        db_table = "Journal"
        db_table_comment = "Contains the ids and names of article journals"
    
    def __str__(self) -> str:
        return f'{self.journal_id}: {self.journal_name}'

class RefType(models.Model): 
    rtype_id = models.AutoField(primary_key=True) 
    rtype_class = models.CharField(max_length=50)
    # edit by Hamid
    #class_description = models.TextField()
    class_description = models.TextField(blank=True, null=True)
    parent_rtype_id=models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='children', blank=True)
    # end of edit by Hamid
    
    class Meta:
        db_table = "Reference-type"
        db_table_comment = "A cyclic table that contains all types of references, the self-joini relation is to indicate whether one reference type is a subcategory of another."

    def __str__(self) -> str: 
        return f'{self.rtpe_id}: {self.rtype_class}:'

class Reference(models.Model): 
    ref_id  = models.AutoField(primary_key=True)
    ref_title = models.CharField(max_length=100)
    full_citation = models.TextField() 
    doi = models.CharField(max_length=50, null=True, blank=True)
    relevance = models.PositiveSmallIntegerField(null=True, blank=True)
    publish_date = models.CharField(max_length=4)
    isbn = models.IntegerField(max_length=15, null=True, blank=True)
    journal_id = models.ForeignKey(Journal, on_delete=models.SET_NULL, null=True, blank=True)
    authors = models.ManyToManyField(Author, blank=True, null=True)
    link = models.CharField(max_length=200, null=True, blank=True) #If given source is a Link 

    class Meta: 
        db_table = "References"
        db_table_comment = "Cotains all reference information"
    
    def __str__(self) -> str: 
        return f'{self.ref_id}: {self.ref_title}'


