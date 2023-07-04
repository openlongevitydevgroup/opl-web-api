import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lpmo.settings')

# Initialize Django
django.setup()

# Import the Theory model after Django setup
from lpmo.models import Theory

Theory.objects.all().delete() 
parent_theory1 = Theory.objects.create(theorytitle='Theories involving DNA', theorydesc='')

child_theory1 = Theory.objects.create(theorytitle='DNA damage (mutation)', theorydesc='', parent_t_id=parent_theory1)
child_theory = Theory.objects.create(theorytitle='mtDNA damage', theorydesc='', parent_t_id=parent_theory1)
child_theory = Theory.objects.create(theorytitle='Telomere shortening', theorydesc='', parent_t_id=parent_theory1)
child_theory = Theory.objects.create(theorytitle='Transposable element activation', theorydesc='', parent_t_id=parent_theory1)
child_theory = Theory.objects.create(theorytitle='Epigenetic modification', theorydesc='', parent_t_id=parent_theory1)
child_theory = Theory.objects.create(theorytitle='Error catastrophe', theorydesc='', parent_t_id=parent_theory1)

parent_theory2 = Theory.objects.create(theorytitle='Accumulation theories', theorydesc='')
child_theory = Theory.objects.create(theorytitle='Clinker theories', theorydesc='', parent_t_id=parent_theory2)
child_theory = Theory.objects.create(theorytitle='Lipofuscin', theorydesc='', parent_t_id=parent_theory2)
child_theory = Theory.objects.create(theorytitle='Cross-links', theorydesc='', parent_t_id=parent_theory2)
child_theory = Theory.objects.create(theorytitle='Advanced glycation end products', theorydesc='', parent_t_id=parent_theory2)
child_theory = Theory.objects.create(theorytitle='Misfolded protein aggregates', theorydesc='', parent_t_id=parent_theory2)
child_theory = Theory.objects.create(theorytitle='Clunker theories', theorydesc='', parent_t_id=parent_theory2)
#child_theory = Theory.objects.create(theorytitle='Mitochondria', theorydesc='', parent_t_id=parent_theory2)
child_theory = Theory.objects.create(theorytitle='Peroxisomes', theorydesc='', parent_t_id=parent_theory2)
child_theory = Theory.objects.create(theorytitle='Lysosomes', theorydesc='', parent_t_id=parent_theory2)

parent_theory3 = Theory.objects.create(theorytitle='Systemic signaling theories', theorydesc='')
child_theory = Theory.objects.create(theorytitle='Endocrine', theorydesc='', parent_t_id=parent_theory3)
child_theory = Theory.objects.create(theorytitle='Immune', theorydesc='', parent_t_id=parent_theory3)
child_theory = Theory.objects.create(theorytitle='Stem cell', theorydesc='', parent_t_id=parent_theory3)

parent_theory4 = Theory.objects.create(theorytitle='Environmental factors', theorydesc='')
child_theory = Theory.objects.create(theorytitle='Hazardous toxic material', theorydesc='', parent_t_id=parent_theory4)
child_theory = Theory.objects.create(theorytitle='Radiations', theorydesc='', parent_t_id=parent_theory4)
child_theory = Theory.objects.create(theorytitle='Germs: Bacteria, Viruses, Fungi, and Protozoa', theorydesc='', parent_t_id=parent_theory4)
child_theory = Theory.objects.create(theorytitle='Interventions', theorydesc='', parent_t_id=parent_theory4)
child_theory = Theory.objects.create(theorytitle='Traumatic Injuries', theorydesc='', parent_t_id=parent_theory4)
child_theory = Theory.objects.create(theorytitle='Nutrition', theorydesc='', parent_t_id=parent_theory4)

parent_theory5 = Theory.objects.create(theorytitle='Oxidative stress and free radical theory of aging', theorydesc='')
parent_theory6 = Theory.objects.create(theorytitle='Inflammaging', theorydesc='')
parent_theory7 = Theory.objects.create(theorytitle='Immune system dysfunction', theorydesc='')
parent_theory8 = Theory.objects.create(theorytitle='Mitochondrial dysfunction', theorydesc='')

# Access the parent theory of a child theory parent_theory = child_theory.parent_t_id # Access the children theories of a parent theory children_theories = parent_theory.children.all() 
all_theories = Theory.objects.all()
for theory in all_theories:
    parent_t_id = theory.parent_t_id.theory_id if theory.parent_t_id else None
    #print(f'{theory}: Parent ID: {parent_t_id}')