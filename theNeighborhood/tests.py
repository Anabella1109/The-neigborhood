from django.test import TestCase
from .models import Neighborhood, Business

class NeighborhoodTestClass(TestCase):
       def setUp(self):
          self.neighborhood=Neighborhood(id=1,name='Rwanda',location='Kigali',occupants=908787)
          


       def tearDown(self):
           Neighborhood.objects.all().delete()
          
       def test_create_neighborhood(self):
           new=Neighborhood.create_neighborhood('ok','hey',1234)
           self.assertIsInstance(new,Neighborhood)

       def test_find_neighborhood(self):
          self.neighborhood.save_neighborhood()
          neighborhood = Neighborhood.find_neighborhood(id=self.neighborhood.id)
          self.assertEquals(neighborhood,self.neighborhood)


           
       def test_save_neighborhood(self):
         self.neighborhood.save_neighborhood()
         neighborhoods = Neighborhood.objects.all()
         self.assertTrue(len(neighborhoods) > 0)   

       def test_delete_neighborhood(self):
           self.neighborhood.save_neighborhood()
           self.neighborhood.delete_neighborhood()
           neighborhoods = Neighborhood.objects.all()
           self.assertTrue(len(neighborhoods) == 0) 

       def test_update_neighborhood(self):
           self.neighborhood.save_neighborhood()
           name='kiki'
           self.neighborhood.update_neighborhood(name)
           self.assertTrue( self.neighborhood.name == name)

       def test_update_occupants(self):
           self.neighborhood.save_neighborhood()
           occupants=234
           self.neighborhood.update_occupants(occupants)
           self.assertTrue( self.neighborhood.occupants == occupants) 

# class ProfileTestClass(TestCase):
#        def setUp(self):
          
#           self.profile=Profile(id=1,photo='Rwanda',bio='Kigali',first_name='hello',last_name='okay',phone_number=908787)
#           self.project=Project(id=1,screenshot='@heroo',name='koko',description="koko koko koko okruuuuuu",overall_grade=2,url='halooooooo')
#           self.grade=Grade(id=1,design=2,usability=2,content=2,project=self.project,total=0,avg=3,comment='olright')
        
#        def tearDown(self):
#           Profile.objects.all().delete()
#           Project.objects.all().delete()
#           Grade.objects.all().delete()
       
#        def test_save_profile(self):
#          self.profile.save_profile()
#          profiles = Profile.objects.all()
#          self.assertTrue(len(profiles) > 0) 

        
#        def test_delete_profile(self):
#            self.profile.save_profile()
#            self.profile.delete_profile()
#            profiles = Profile.objects.all()
#            self.assertTrue(len(profiles) == 0)  

#        def test_update_bio(self):
#            self.profile.save_profile()
#            bio='kiki'
#            self.profile.update_bio(bio)
#            self.assertTrue( self.profile.bio == bio) 


class BusinessTestClass(TestCase):
       def setUp(self):
           self.neighborhood=Neighborhood(id=1,name='Rwanda',location='Kigali',occupants=908787)
           self.business=Business(id=1,name='Rwanda',location='Kigali',neighborhood=self.neighborhood,email='jjj@gmail.com',phone_number=98865746)


       def tearDown(self):
          Neighborhood.objects.all().delete()
          Business.objects.all().delete()


       def test_create_business(self):
           self.neighborhood.save_neighborhood()
           new=Business.create_business('ok','hey',self.neighborhood ,'nnn',1234)
           self.assertIsInstance(new,Business)
         
        
  
#        def test_save_grade(self):
#          self.profile.save_profile()
#          self.project.save_project()
#          self.grade.save_grade()
#          grades = Grade.objects.all()
#          self.assertTrue(len(grades) > 0) 

        
#        def test_delete_grade(self):
#            self.profile.save_profile()
#            self.project.save_project()
#            self.grade.save_grade()
#            self.grade.delete_grade()
#            grades = Grade.objects.all()
#            self.assertTrue(len(grades) == 0)  

#        def test_update_comment(self):
#            self.profile.save_profile()
#            self.project.save_project()
#            self.grade.save_grade()
#            comment='kiki'
#            self.grade.update_comment(comment)
#            self.assertTrue( self.grade.comment == comment) 



# Create your tests here.


# Create your tests here.
