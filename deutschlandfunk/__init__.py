# -*- coding: utf-8 -*-

import requests

from bs4 import BeautifulSoup

from . import urls

def get_broadcasts():
	broadcasts_a_to_z_request = requests.get(urls.BROADCASTS_A_TO_Z_URL)
	assert(
		broadcasts_a_to_z_request.ok,
		f"Could not get {urls.BROADCASTS_A_TO_Z_URL}: error {broadcasts_a_to_z_request.status_code}"
	)
	
	broadcasts_a_to_z_soup = BeautifulSoup(broadcasts_a_to_z_request.text, features="html.parser")

