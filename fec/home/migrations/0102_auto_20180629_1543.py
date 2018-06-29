# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import home.blocks
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0101_auto_20180531_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='custompage',
            name='related_topics',
            field=wagtail.core.fields.StreamField((('related_topics', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(label='Related topic'))),), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='collectionpage',
            name='reporting_examples',
            field=wagtail.core.fields.StreamField((('reporting_examples', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('content', wagtail.core.blocks.RichTextBlock(help_text='Use Shift + Enter to add line breaks between citation and description')))))),), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='custompage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('example_paragraph', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=True)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=True))))), ('example_forms', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=True)), ('forms', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.core.blocks.URLBlock()), ('media_type', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.CharBlock())))))))), ('reporting_example_cards', wagtail.core.blocks.StructBlock((('card_width', wagtail.core.blocks.ChoiceBlock(choices=[(2, '1/2'), (3, '1/3')], help_text='Control the width of the cards')), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(), icon='doc-empty'))))), ('contact_info', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock(icon='title', required=False)), ('contact_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('item_label', wagtail.core.blocks.CharBlock(required=False)), ('item_icon', wagtail.core.blocks.ChoiceBlock(choices=[('email', 'Email'), ('fax', 'Fax'), ('hand', 'Hand delivery'), ('phone', 'Phone'), ('mail', 'Mail'), ('github', 'Github'), ('question-bubble', 'Question')])), ('item_info', wagtail.core.blocks.RichTextBlock(required=True))))))))), ('internal_button', wagtail.core.blocks.StructBlock((('internal_page', wagtail.core.blocks.PageChooserBlock()), ('text', wagtail.core.blocks.CharBlock())))), ('external_button', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.URLBlock()), ('text', wagtail.core.blocks.CharBlock())))), ('contribution_limits_table', wagtail.snippets.blocks.SnippetChooserBlock('home.EmbedTableSnippet', icon='table', template='blocks/embed-table.html')))),
        ),
        migrations.AlterField(
            model_name='custompage',
            name='citations',
            field=wagtail.core.fields.StreamField((('citations', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('content', wagtail.core.blocks.RichTextBlock(help_text='Use Shift + Enter to add line breaks between citation and description')))))),), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='custompage',
            name='continue_learning',
            field=wagtail.core.fields.StreamField((('continue_learning', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.core.blocks.URLBlock()), ('media_type', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.CharBlock()))), icon='doc-empty')),), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='custompage',
            name='date',
            field=models.DateField(verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='custompage',
            name='record_articles',
            field=wagtail.core.fields.StreamField((('record_articles', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(target_model=['home.RecordPage']))),), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='citations',
            field=wagtail.core.fields.StreamField((('citations', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('content', wagtail.core.blocks.RichTextBlock(help_text='Use Shift + Enter to add line breaks between citation and description')))))),), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='intro',
            field=wagtail.core.fields.StreamField((('paragraph', wagtail.core.blocks.RichTextBlock()),), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='related_topics',
            field=wagtail.core.fields.StreamField((('related_topics', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(label='Related topic'))),), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='sections',
            field=wagtail.core.fields.StreamField((('sections', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=True)), ('hide_title', wagtail.core.blocks.BooleanBlock(help_text='Should the section title be displayed?', required=False)), ('content', wagtail.core.blocks.StreamBlock((('text', wagtail.core.blocks.RichTextBlock(blank=False, icon='pilcrow', null=False, required=False)), ('documents', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.core.blocks.URLBlock()), ('media_type', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.CharBlock()))), icon='doc-empty', template='blocks/section-documents.html')), ('contact_info', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock(icon='title', required=False)), ('contact_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('item_label', wagtail.core.blocks.CharBlock(required=False)), ('item_icon', wagtail.core.blocks.ChoiceBlock(choices=[('email', 'Email'), ('fax', 'Fax'), ('hand', 'Hand delivery'), ('phone', 'Phone'), ('mail', 'Mail'), ('github', 'Github'), ('question-bubble', 'Question')])), ('item_info', wagtail.core.blocks.RichTextBlock(required=True))))))))), ('internal_button', wagtail.core.blocks.StructBlock((('internal_page', wagtail.core.blocks.PageChooserBlock()), ('text', wagtail.core.blocks.CharBlock())))), ('external_button', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.URLBlock()), ('text', wagtail.core.blocks.CharBlock())))), ('page', wagtail.core.blocks.PageChooserBlock(template='blocks/page-links.html')), ('disabled_page', wagtail.core.blocks.CharBlock(blank=False, help_text='Name of a disabled link', icon='placeholder', null=False, required=False, template='blocks/disabled-page-links.html')), ('document_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock()))), icon='doc-empty', template='blocks/document-list.html')), ('current_commissioners', home.blocks.CurrentCommissionersBlock()), ('fec_jobs', home.blocks.CareersBlock()), ('mur_search', home.blocks.MURSearchBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('reporting_example_cards', wagtail.core.blocks.StructBlock((('card_width', wagtail.core.blocks.ChoiceBlock(choices=[(2, '1/2'), (3, '1/3')], help_text='Control the width of the cards')), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(), icon='doc-empty'))))), ('contribution_limits_table', wagtail.snippets.blocks.SnippetChooserBlock('home.EmbedTableSnippet', icon='table', template='blocks/embed-table.html'))))), ('aside', wagtail.core.blocks.StreamBlock((('title', wagtail.core.blocks.CharBlock(icon='title', required=False)), ('document', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.core.blocks.URLBlock()), ('media_type', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.CharBlock())))), ('link', wagtail.core.blocks.StructBlock((('link_type', wagtail.core.blocks.ChoiceBlock(choices=[('calculator', 'Calculator'), ('calendar', 'Calendar'), ('record', 'Record'), ('search', 'Search')], help_text='Set an icon', icon='link', required=False)), ('url', wagtail.core.blocks.URLBlock()), ('text', wagtail.core.blocks.CharBlock(required=True)), ('coming_soon', wagtail.core.blocks.BooleanBlock(required=False)))))), icon='placeholder', required=False, template='blocks/section-aside.html'))))), ('image', wagtail.images.blocks.ImageChooserBlock())), blank=True, null=True),
        ),
    ]
