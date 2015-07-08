from django.test import TestCase
from django.utils import timezone

from .models import Campaign, Session, Note, Character

import random

# Create your tests here.
class SessionsModelsTest(TestCase):
    pass

class SessionsViewsTest(TestCase):
    def setUp(self):
        """create dummy data"""
        c = Campaign.objects.create(name="TestName", date=timezone.now(), system="Star Wars: D6")
        s = Session.objects.create(date=timezone.now(), campaign=c)
        char = Character.objects.create(name="TwinHits", campaign=c)
        cn = Note(content_object=c, text="campaign note", date=timezone.now())
        cn.save()
        sn = Note(content_object=s, text="session note", date=timezone.now())
        sn.save()
        chn = Note(content_object=char, text="character note", date=timezone.now())
        chn.save()


    def test_home(self):
        """Test the home page, comparing list of all campaigns vs campaigns provided to view"""
        resp = self.client.get("/sessions/")
        self.assertEqual(resp.status_code, 200) 
        self.assertTrue("campaigns" in resp.context)
        self.assertListEqual(list(Campaign.objects.all()), list(resp.context["campaigns"]))


    def test_campaign_detail(self):
        """Test the campaign view with a random campaign"""
        c = random.choice(Campaign.objects.all())
        #test 200 and data transfer
        resp = self.client.get("/sessions/" + str(c.pk) + "/")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("campaign" in resp.context)
        self.assertTrue("sessions" in resp.context)
        self.assertTrue("notes" in resp.context)
        self.assertTrue("characters" in resp.context)
        #test campaign pk's on all data
        self.assertEqual(c.pk, resp.context["campaign"].pk)
        [self.assertTrue(s.campaign, c.pk) for s in resp.context["sessions"]]
        [self.assertTrue(n.object_id, c.pk) for n in resp.context["notes"]] 
        [self.assertTrue(ch.campaign, c.pk) for ch in resp.context["characters"]]
        #test 404
        resp = self.client.get("sessions/" + str(len(Campaign.objects.all()) + 1) + "/")
        self.assertEqual(resp.status_code, 404)


    def test_session_detail(self):
        """Test the session detail page wth a random session."""
        s = random.choice(Session.objects.all())
        #test 200 and data transfer
        resp = self.client.get("/sessions/" + str(s.campaign.pk) + "/session/" + str(s.pk) + "/")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("campaign" in resp.context)
        self.assertTrue("session" in resp.context)
        self.assertTrue("notes" in resp.context)
        #test session pk's on all data
        self.assertTrue(s.pk, resp.context["session"].pk)
        self.assertEqual(s.campaign.pk, resp.context["campaign"].pk)
        [self.assertTrue(n.object_id, s.pk) for n in resp.context["notes"]]

    def test_character_detail(self):
        """Test the character detail page with a random character."""
        ch = random.choice(Character.objects.all())
        #test 200 and data transfer
        resp = self.client.get("/sessions/" + str(ch.campaign.pk) + "/character/" + str(ch.pk) + "/")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("character" in resp.context)
        self.assertTrue("notes" in resp.context)
        #test character pk's on all data
        self.assertTrue(ch.pk, resp.context["character"].pk)
        [self.assertTrue(n.object_id, ch.pk) for n in resp.context["notes"]]

    def test_campaign_new(self):
        resp = self.client.post("/sessions/new/", {"name": "", "date": "", "system": ""})
        self.assertFormError(resp, "form", "name", "This field is required.")
        self.assertFormError(resp, "form", "date", "This field is required.")
        self.assertFormError(resp, "form", "system", "This field is required.")
        
