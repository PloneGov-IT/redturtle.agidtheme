# -*- coding: utf-8 -*-
from plone.supermodel import model
from redturtle.agidtheme import _
from zope import schema


class IRedturtleAgidthemeSettings(model.Schema):

    available_types = schema.List(
        title=_(u'heading_available_portaltypes',
                default=u'Shareable content types'),
        description=_(u'description_available_portaltypes',
                      default=u'List of content-types that can be enable '
                              u'for social sharing.'),
        required=False,
        default=[],
        missing_value=[],
        value_type=schema.Choice(
            vocabulary='plone.app.vocabularies.UserFriendlyTypes'
        )
    )

    available_socials = schema.List(
        title=_(u'heading_available_socials',
                default=u'Enabled social networks'),
        description=_(u'description_available_socials',
                      default=u'List of social networks enabled for sharing.'),
        required=False,
        default=[],
        missing_value=[],
        value_type=schema.Choice(
            vocabulary='redturtle.agidtheme.vocabularies.SocialsVocabulary'
        )
    )

    header_link_label = schema.TextLine(
        title=_(u'header_link_label',
                default=u'Header link label'),
        description=_(u'header_link_label_desc',
                      default=u'Label for the link in the header of the site'),
        required=False
    )

    header_facebook_link = schema.TextLine(
        title=_(u'header_facebook_link_label',
                default=u'Facebook page link'),
        description=_(u'header_facebook_link_desc',
                      default=u'Link to Facebook page to show in the header.'),
        required=False
    )

    header_twitter_link = schema.TextLine(
        title=_(u'header_twitter_link_label',
                default=u'Twitter link'),
        description=_(u'header_twitter_link_desc',
                      default=u'Link to Twitter account to show in the header.'),  # noqa
        required=False
    )

    header_youtube_link = schema.TextLine(
        title=_(u'header_youtube_link_label',
                default=u'YouTube link'),
        description=_(u'header_youtube_link_desc',
                      default=u'Link to YouTube to show in the header.'),
        required=False
    )

    header_link_url = schema.URI(
        title=_(u'header_link_url',
                default=u'Header link url'),
        description=_(u'header_link_url_desc',
                      default=u'URL of the link in the header'),
        required=False
    )

    header_second_link_label = schema.TextLine(
        title=_(u'header_second_link_label',
                default=u'Header second link label'),
        description=_(u'header_second_link_label_desc',
                      default=u'Label for the link in the header of\
                              the site at right'),
        required=False
    )

    header_second_link_url = schema.URI(
        title=_(u'header_second_link_url',
                default=u'Header second link url'),
        description=_(u'header_second_link_url_desc',
                      default=u'URL of the link in the header at right'),
        required=False
    )
