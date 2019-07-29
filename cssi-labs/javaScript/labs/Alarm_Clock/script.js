// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

console.log("script is running...");

function myAlarm(wakeup)
{
  console.log("Hey, Adam, wake up! It's" + wakeup);
}
 myAlarm(" 6am")
 
 function momAlarm(wakeup2)
 {
   console.log("Hey, Mom, wake up! It's" + wakeup2);
 }
  momAlarm(" 5:30am")

function familyAlarm (wakeup, wakeup2)
{
    console.log("Hey, Adam, wake up! It's" + wakeup);
    console.log("Hey, Mom, wake up! It's" + wakeup2);
}
familyAlarm ("6am","5:30am")

function importantAlarm (Wakeup3) 
{
    return Wakeup3.toUpperCase();
}
console.log(importantAlarm("wake up, wake up, wake UP!!"))

function snoozeAlarm (wakeup5)
{
    var newtime=wakeup5 + 1;
    return "The alarm for "+wakeup5+" has been changed to "+newtime;

}
console.log(snoozeAlarm("6am"))