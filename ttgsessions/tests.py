from django.test import TestCase
from django.utils import timezone

from .models import Campaign, Session, Note

import random

# Create your tests here.
class SessionsModelsTest(TestCase):
    pass

class SessionsViewsTest(TestCase):
    def setUp(self):
        """create dummy data"""
        c = Campaign.objects.create(name="TestName", start_date=timezone.now())
        s = Session.objects.create(sess_date=timezone.now(), campaign=c)
        cn = Note(content_object=c, note_text="campaign note", pub_date=timezone.now())
        cn.save()
        sn = Note(content_object=s, note_text="session note", pub_date=timezone.now())
        sn.save()


    def test_home(self):
        """Test the home page"""
        resp = self.client.get("/sessions/")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("campaigns" in resp.context)


    def test_campaign_detail(self):
        """Test the campaign view with a random campaign"""
        campaigns = Campaign.objects.all() 
        c = random.choice(campaigns)
        #test 200 and data validity
        resp = self.client.get("/sessions/" + str(c.pk) + "/")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("campaign" in resp.context)
        self.assertTrue("sessions" in resp.context)
        self.assertTrue("notes" in resp.context)
        #test campaign pk's on all data
        self.assertEqual(c.pk, resp.context["campaign"].pk)
        [self.assertTrue(s.campaign, c.pk) for s in resp.context["sessions"]]
        [self.assertTrue(n.object_id, c.pk) for n in resp.context["notes"]]
        #test 404
        resp = self.client.get("sessions/" + str(len(campaigns) + 1) + "/")
        self.assertEqual(resp.status_code, 404)


    def test_session_detail(self):
        """Test the session detail page wth a random session."""
        s = random.choice(Session.objects.all())
        #test 200 and data validity
        resp = self.client.get("/sessions/" + str(s.campaign.pk) + "/" + str(s.pk) + "/")
        print("/sessions/" + str(s.campaign.pk) + "/" + str(s.pk) + "/")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("campaign" in resp.context)
        self.assertTrue("session" in resp.context)
        self.assertTrue("notes" in resp.context)
        #test session pk's on all data
        self.assertTrue(s.pk, resp.context["session"].pk)
        self.assertEqual(s.campaign.pk, resp.context["campaign"].pk)
        [self.assertTrue(n.object_id, s.pk) for n in resp.context["notes"]]
