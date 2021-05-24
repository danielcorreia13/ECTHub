# Generated by Django 3.2.3 on 2021-05-24 16:05

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subjects',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('p1', 'Programação 1'), ('isd', 'Introdução aos Sistemas Digitais'), ('c1', 'Cálculo 1'), ('alga', 'Álgebra Linear e Geometria Analítica'), ('labi', 'Laboratórios de Informática'), ('p2', 'Programação 2'), ('lsd', 'Laboratórios de Sistemas Digitais'), ('md', 'Matemática Discreta'), ('c2', 'Cálculo 2'), ('p3', 'Programação 3'), ('ac1', 'Arquitetura de Computadores 1'), ('mce', 'Mecânica e Campo Eletromagnético'), ('mpei', 'Métodos Probabilísticos para Engenharia Informática'), ('ac2', 'Arquitetura de Computadores 2'), ('se', 'Sistemas Eletrónicos'), ('lfa', 'Linguagens Formais e Autómatos'), ('algc', 'Algoritmos e Complexidade'), ('iia', 'Introdução à Inteligência Artificial'), ('fr', 'Fundamentos de Redes'), ('ams', 'Análise e Modelação de Sistemas'), ('so', 'Sistemas de Operação'), ('ihc', 'Interação Humano-Computador'), ('pei', 'Projecto em Engenharia Informática'), ('ar', 'Arquitectura de Redes'), ('bd', 'Base de Dados'), ('ara', 'Arquitetura de Redes Avançada'), ('aca', 'Arquitetura de Computadores Avançada'), ('edc', 'Engenharia de Dados e Conhecimento'), ('cv', 'Computação Visual'), ('s', 'Segurança'), ('sd', 'Sistemas Distribuídos'), ('es', 'Engenharia de Software'), ('cr', 'Computação Reconfigurável'), ('ddr', 'Desempenho e Dimensionamento de Redes'), ('gpe', 'Gestão de Projectos e Empreendorismo'), ('tese', 'Dissertação')], max_length=131),
        ),
    ]