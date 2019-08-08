#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import random
import jinja2
import logging 

def get_fortune():
    fortunes=['You will find riches.',
            'You will die alone.',
            'Tomorrow will be your best day ever.',
            'Your dream job will offer you an interview.',
            'You will meet your soulmate.',
            'You declare BANKRUPTCY!',
            'Dark times ahead my friend...',
            'A friend will betray you.',
            'A lifelong friend will reveal themselves.',
            'Keep your guard up.',]
    i = random.randint(0,len(fortunes)-1)
    random_fortune= fortunes[i]
    return random_fortune

# Remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        # In part 2, instead of returning this string,
        # make a function call that returns a random fortune.
        logging.info("hi this is a message")
        results_template = jinja_current_directory.get_template("templates/fortune-start.html")
        self.response.write(results_template.render())
    # Add a post method
    def post(self):
        logging.info("The users astro sign is " + 'user_astro_sign')
        x = get_fortune()
        user_astro_sign = self.request.get("user_astrological_sign")
        fortune_dict={'fortune':x, 'astro_sign':user_astro_sign}
        end_template = jinja_current_directory.get_template("templates/fortune-results.html")
        self.response.write(end_template.render(fortune_dict))
     

class HelloHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello World. Welcome to the root route of my app')

class GoodbyeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('My response is Goodbye World')
# Route mapping
app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', HelloHandler),
    ('/predict', FortuneHandler), #maps '/predict' to the FortuneHandler
    ('/farewell', GoodbyeHandler),
], debug=True)
