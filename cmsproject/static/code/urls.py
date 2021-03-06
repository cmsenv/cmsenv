# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.conf.urls.static import static
from quanti.views import *

urlpatterns = [
	url(r'^adminmail',adminmail),
	url(r'^adminsms', adminsms),
	url(r'^adminpage', adminpage),
	url(r'^logoutadmin',adminlogout),
    url(r'^administration', administration),
	url(r'^admin', include(admin.site.urls)),
	url(r'^page404', page404),
	url(r'^about1', about1),
	url(r'^about2', about2),
	url(r'^about3', about3),
	url(r'^about4', about4),
	url(r'^about5', about5),
	url(r'^alerts-and-wells', alertsandwells),
	url(r'^backtesting',backtesting),
	url(r'^blog_grid_col_2', blog_grid_col_2),
	url(r'^blog_grid_col_3', blog_grid_col_3),
	url(r'^blog_grid_col_4', blog_grid_col_4),
	url(r'^blog_grid_masonry_col_2', blog_grid_masonry_col_2),
	url(r'^blog_grid_masonry_col_3', blog_grid_masonry_col_3),
	url(r'^blog_grid_masonry_col_4', blog_grid_masonry_col_4),
	url(r'^blog_single_left_sidebar', blog_single_left_sidebar),
	url(r'^blog_single_right_sidebar', blog_single_right_sidebar),
	url(r'^blog_standard_left_sidebar', blog_standard_left_sidebar),
	url(r'^blog_standard_right_sidebar', blog_standard_right_sidebar),
	url(r'^buttons', buttons),
	url(r'^callback',callback),
	url(r'^changedetails',changedetails),
	url(r'^check', check),
	url(r'^contact1', contact1),
	url(r'^contact2', contact2),
	url(r'^contact3', contact3),
	url(r'^content_box', content_box),
	url(r'^documentation', documentation),
	url(r'^faq', faq),
	url(r'^filesystem', filesystem),
	url(r'^forms', forms),
	url(r'^gallery_col_2', gallery_col_2),
	url(r'^gallery_col_3', gallery_col_3),
	url(r'^gallery_col_4', gallery_col_4),
	url(r'^gallery_col_6', gallery_col_6),
	url(r'^getintouch',getintouch),
	url(r'^icons', icons),
	url(r'^index_agency', index_agency),
	url(r'^index_finance', home),
	url(r'^index_landing', index_landing),
	url(r'^index_mp_classic_flexslider', index_mp_classic_flexslider),
	url(r'^index_mp_classic_gradient_overlay', index_mp_classic_gradient_overlay),
	url(r'^index_mp_classic_static', index_mp_classic_static),
	url(r'^index_mp_classic_text_rotator', index_mp_classic_text_rotator),
	url(r'^index_mp_classic_video_background', index_mp_classic_video_background),
	url(r'^index_mp_fullscreen_flexslider', index_mp_fullscreen_flexslider),
	url(r'^index_mp_fullscreen_gradient_overlay', index_mp_fullscreen_gradient_overlay),
	url(r'^index_mp_fullscreen_static', index_mp_fullscreen_static),
	url(r'^index_mp_fullscreen_text_rotator', index_mp_fullscreen_text_rotator),
	url(r'^index_mp_fullscreen_video_background', index_mp_fullscreen_video_background),
	url(r'^index_op_fullscreen_gradient_overlay', index_op_fullscreen_gradient_overlay),
	url(r'^index_photography', index_photography),
	url(r'^index_portfolio', index_portfolio),
	url(r'^index_restaurant', index_restaurant),
	url(r'^index_shop', index_shop),
    url(r'^index', index),
	url(r'^login_register', login_register),
	url(r'^logout',logout),
	url(r'^notebook',notebook),
	url(r'^partnership',partnership),
	url(r'^partnerrequest',partnerrequest),
	url(r'^portfolio_boxed_col_2', portfolio_boxed_col_2),
	url(r'^portfolio_boxed_col_3', portfolio_boxed_col_3),
	url(r'^portfolio_boxed_col_4', portfolio_boxed_col_4),
	url(r'^portfolio_boxed_gutter_col_2', portfolio_boxed_gutter_col_2),
	url(r'^portfolio_boxed_gutter_col_3', portfolio_boxed_gutter_col_3),
	url(r'^portfolio_boxed_gutter_col_4', portfolio_boxed_gutter_col_4),
	url(r'^portfolio_full_width_col_2', portfolio_full_width_col_2),
	url(r'^portfolio_full_width_col_3', portfolio_full_width_col_3),
	url(r'^portfolio_full_width_col_4', portfolio_full_width_col_4),
	url(r'^portfolio_full_width_gutter_col_2', portfolio_full_width_gutter_col_2),
	url(r'^portfolio_full_width_gutter_col_3', portfolio_full_width_gutter_col_3),
	url(r'^portfolio_full_width_gutter_col_4', portfolio_full_width_gutter_col_4),
	url(r'^portfolio_hover_black', portfolio_hover_black),
	url(r'^portfolio_hover_gradient', portfolio_hover_gradient),
	url(r'^portfolio_masonry_boxed_col_2', portfolio_masonry_boxed_col_2),
	url(r'^portfolio_masonry_boxed_col_3', portfolio_masonry_boxed_col_3),
	url(r'^portfolio_masonry_boxed_col_4', portfolio_masonry_boxed_col_4),
	url(r'^portfolio_masonry_full_width_col_2', portfolio_masonry_full_width_col_2),
	url(r'^portfolio_masonry_full_width_col_3', portfolio_masonry_full_width_col_3),
	url(r'^portfolio_masonry_full_width_col_4', portfolio_masonry_full_width_col_4),
	url(r'^portfolio_single_featured_image1', portfolio_single_featured_image1),
	url(r'^portfolio_single_featured_image2', portfolio_single_featured_image2),
	url(r'^portfolio_single_featured_slider1', portfolio_single_featured_slider1),
	url(r'^portfolio_single_featured_slider2', portfolio_single_featured_slider2),
	url(r'^portfolio_single_featured_video1', portfolio_single_featured_video1),
	url(r'^portfolio_single_featured_video2', portfolio_single_featured_video2),
	url(r'^pricing1', pricing1),
	url(r'^pricing2', pricing2),
	url(r'^promotionmail', promotionmail),
	url(r'^progressbars', progressbars),
	url(r'^restaurant_menu1', restaurant_menu1),
	url(r'^restaurant_menu2', restaurant_menu2),
	url(r'^search',search),
	url(r'^sendsms', smssend),
	url(r'^service1', service1),
	url(r'^service2', service2),
	url(r'^service3', service3),
	url(r'^shop_checkout', shop_checkout),
	url(r'^shop_product_col_3', shop_product_col_3),
	url(r'^shop_product_col_4', shop_product_col_4),
	url(r'^shop_single_product', shop_single_product),
	url(r'^signup', insert),
	url(r'^tabs_and_accordions', tabs_and_accordions),
	url(r'^taggit_autosuggest', include('taggit_autosuggest.urls')),
	url(r'^typography', typography),
	url(r'^userlist', userlist),
	url(r'^user_profile', user_profile),
	url(r'^validate', validate),
	
	#url(r'^', include('cms.urls'))
	url(r'^', home)
]

# This is only needed when using runserver.
if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
