#!/usr/bin/env python

import os

import mailroom_4 as mailroom

donors = {}
donors['Kevin Cavanaugh'] = (500.55, 899.34, 78.94)
donors['Victor Murphy'] = (99.89, 87.02)
donors['Randy Brown'] = (10.11, 1000.01, 99.99)
donors['Piper Long'] = (190.99, 100.02)
donors['Kim Pinkie'] = (2344.44, 8999.66, 345.55)


def test_donor_list():
    listing = mailroom.create_donor_list()
    assert "Kevin Cavanaugh" in listing
    assert len(listing.split('\n')) == 7
    assert listing.startswith("Donors: \n")


def test_create_report():
    report = mailroom.create_report(donors)
    assert report.startswith('Donor                |Total           |Num Gifts  |Average Gift')


def test_add_donation():
    name = "Randal Root"
    donation = "500"
    mailroom.add_donation(donors, name, donation)
    assert donors['Randal Root']


def test_write_letter():
    mailroom.write_letters()
    assert os.path.isdir('thank_you_letters')

