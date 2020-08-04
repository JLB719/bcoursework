from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase) :
    def setUp(self) :
        self.browser = webdriver.Firefox()

    def tearDown(self) :
        self.browser.quit()
    def check_in_table(self, row_text, idtag) :
        table = self.browser.find_element_by_id(idtag)
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])



    def test_can_build_a_cv(self) :
        #goes to check out cv builder
        self.browser.get('http://localhost:8000')
        #notices title and header mention cv builder
        self.assertIn('CV Builder', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1')

        #invited to enter name
        inputboxname=self.browser.find_element_by_id('name')
        self.assertEqual(self.browser.find_element_by_id('namequestion').text, 'Enter your full name')
        #types James Bartlett into text box
        inputboxname.send_keys('James Bartlett')

        #invited to enter mobile number into text box
        inputboxnumber=self.browser.find_element_by_id('number')
        self.assertEqual(self.browser.find_element_by_id('telquestion').text, 'Enter your telephone number')
        #types 111111111 into text text box
        inputboxnumber.send_keys('111111111')
        #invited to enter email into text box
        inputboxemail = self.browser.find_element_by_id('email')
        self.assertEqual(self.browser.find_element_by_id('emailquestion').text, "Enter your email")
        # enters james@gmail.com
        inputboxemail.send_keys('james@gmail.com')

        submitpersonaldetails = self.browser.find_element_by_id('details')
        submitpersonaldetails.click()
        # when hits enter name, email and number are displayed
        self.assertEqual(self.browser.find_element_by_id('namedis').text, 'James Bartlett')
        self.assertEqual(self.browser.find_element_by_id('emaildis').text, 'james@gmail.com')
        self.assertEqual(self.browser.find_element_by_id('numberdis').text, '111111111')
        #will need to decide how i want it displayed
        #Personal profile

        #Invited towrite a personal profile
        inputboxprofile = self.browser.find_element_by_id('personalprof')
        self.assertEqual(self.browser.find_element_by_id('profquestion').text, 'Enter a personal profile')
        #Types looking for work have a computer sciecne degree and good teamwork skills
        inputboxprofile.send_keys('Looking for work have a computer science degree and good teamwork skills')
        submitprofile = self.browser.find_element_by_id('Profile')
        submitprofile.click()
        #Upon enter personal profile is displayed
        self.assertEqual(self.browser.find_element_by_id('profiledis').text, 'Looking for work have a computer science degree and good teamwork skills')
        #Skills
        inputboxskills=self.browser.find_element_by_id('skill')
        self.assertEqual(self.browser.find_element_by_id('Skillsquestion').text, 'Enter a skill')

        #Invited to enter a skill
        inputboxskills.send_keys('Java')
        inputboxskills.send_keys(Keys.ENTER)
        #Types Java

        # Upon enter java is displayed underskills
        self.check_in_table('Java', 'skillstable')
        # Invited to enter another skill
        inputboxskills=self.browser.find_element_by_id('skill')

        # Types Teamwork
        inputboxskills.send_keys('Teamwork')
        inputboxskills.send_keys(Keys.ENTER)
        # Upon enter both skills entries are displayed
        self.check_in_table('Java', 'skillstable')
        self.check_in_table('Teamwork', 'skillstable')
        #Achievments

        # Invited to enter an achievment
        inputboxachievments=self.browser.find_element_by_id('achievment')
        self.assertEqual(self.browser.find_element_by_id('Achievmentquestion').text, 'Enter an achievment')

        # Types 1st place in hackathon
        inputboxachievments.send_keys('1st place in hackathon')
        # Upon enter displays ahcivment
        inputboxachievments.send_keys(Keys.ENTER)
        self.check_in_table('1st place in hackathon', 'achtable')
        # Invited to enter another achievent
        inputboxachievments=self.browser.find_element_by_id('achievment')
        #Types a levels
        inputboxachievments.send_keys('a levels')

        # upon enter displays both ahcivments
        inputboxachievments.send_keys(Keys.ENTER)
        self.check_in_table('1st place in hackathon', 'achtable')

        self.check_in_table('a levels', 'achtable')
        #Work experience

        # Invited to enter name of company
        inputboxcompany = self.browser.find_element_by_id('placeofwork')
        self.assertEqual(self.browser.find_element_by_id('placeofworkq').text, 'Enter the place of work')
        #Enters university of brimigham
        inputboxcompany.send_keys("University of Birmingham")
        # Invited to enter job role
        inputboxjob = self.browser.find_element_by_id('role')
        self.assertEqual(self.browser.find_element_by_id('roleq').text, 'Enter the job role')
        #Types student ambassador
        inputboxjob.send_keys("student ambassador")
        #Invited to enter date started
        inputboxstartdatew=self.browser.find_element_by_id('startdatew')
        self.assertEqual(self.browser.find_element_by_id('startdatewq').text, 'Enter the start date of the job')

        #Types 01/2019
        inputboxstartdatew.send_keys('01/01/2019')
        #Invited to enter date finished or present
        inputboxenddatew=self.browser.find_element_by_id('enddatew')
        self.assertEqual(self.browser.find_element_by_id('enddatewq').text, 'Enter the date you finished the role')
        #Types present
        inputboxenddatew.send_keys('03/08/2020')
        #Invited to enter job description
        inputboxjobdes=self.browser.find_element_by_id('description')
        self.assertEqual(self.browser.find_element_by_id('jobdesq').text, 'Enter the job description details')

        #Types resonsiple to showing students round builidng makeing them feel welcome and setting up events
        inputboxjobdes.send_keys("Responsible for showing students round building making them feel welcome and setting up events")
        submitworkexp = self.browser.find_element_by_id('WorkExperience')
        submitworkexp.click()
        #Upon enter company, role, dates and job description are displayed
        self.assertEqual(self.browser.find_element_by_id('jobtitled').text, "student ambassador")
        self.assertEqual(self.browser.find_element_by_id('jobcomd').text, "University of Birmingham")
        self.assertEqual(self.browser.find_element_by_id('jobdatesd').text, "01/01/2019-03/08/2020")
        self.assertEqual(self.browser.find_element_by_id('jobdetailsd').text, "Responsible for showing students round building making them feel welcome and setting up events")

        #Education

        #Invited to enter place of learning
        inputboxschool=self.browser.find_element_by_id('school')
        self.assertEqual(self.browser.find_element_by_id('schoolq').text, 'Enter the name of the school')

        #Enters woodhouse college
        inputboxschool.send_keys('Woodhouse College')
        # Invited to enter date started
        inputboxstartdates=self.browser.find_element_by_id('startdates')
        self.assertEqual(self.browser.find_element_by_id('startdatesq').text, 'Enter the date you started at the school')

        #Types 09/2016
        inputboxstartdates.send_keys('01/09/2016')
        #Invited to enter date left
        inputboxenddates=self.browser.find_element_by_id('enddates')
        self.assertEqual(self.browser.find_element_by_id('enddatesq').text, 'Enter the date you finished at the school')

        #Types 07/2018
        inputboxenddates.send_keys('01/07/2018')
        #Invited to enter qualifications
        inputboxgrades = self.browser.find_element_by_id('grades')
        self.assertEqual(self.browser.find_element_by_id('gradesq').text, 'Enter the grades obtained')

        #Types Maths A* FUther Maths B, Georgraphy A
        inputboxgrades.send_keys('Maths A* Further Maths B Georgraphy A')
        # Upon enter school, dates and grades are displayed
        submiteducation=self.browser.find_element_by_id('EducationSubmit')
        submiteducation.click()
        self.assertEqual(self.browser.find_element_by_id('schoold').text, "Woodhouse College")
        self.assertEqual(self.browser.find_element_by_id('schooldatesd'), "01/09/2016-01/07/2018")
        self.assertEqual(self.browser.find_element_by_id('schooldetailsd'), 'Maths A* Further Maths B Georgraphy A')

	# def test_can_edit_a_cv(self) :

		#Deletes the skill programming

		#Upon click of button programming skill is deleted

		#Invited to remove ahievement

		#Deltes a level achievment

		#Upon delteion achievments are listed without a level ahcivment

		#Invited to add more work experience

		#Invited to add company

		#Types PGL

		#Invited to add job role

		#Types acitvity insturuction / group leader

		#Invited to add start date

		#types 07/2019

		#Invited to add end date

		#types 09/2019

		#invited to add job description

		#types responsible for looking after kids, leading them on hikes and helping out in the center

		#Upon enter both peices of work expereicne are displayed

		#invited to delete work expeirece

		# deltes peice of work expeirece

		# page is updated to no long display that work experience

		#invited to edit personal profile

		# changes it to currently a student looking for more accademic work

		# upon enter page is updated to display the changed information

		# invited to add education

		# invited to add name of school

		# types University of Birmignham

		# invited to add year started

		# types 09/2018

		# invited to add year finished

		# types  08/2022

		# invited to add qualifcations obtained or predicted qualifcations

		# upon enter page is updated




if __name__ == '__main__' :
    unittest.main(warnings='ignore')
