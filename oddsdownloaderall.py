#goes through all bookmaker odds and parses them into CSV

import time
from selenium import webdriver
import csv

start=time.time()

driver = webdriver.Chrome(r"/usr/local/bin/chromedriver")
driver.get("https://bonusbagging.co.uk/oddsmatching.php"); #go to site
main_window = driver.current_window_handle
driver.switch_to_window(main_window)
time.sleep(0.25) # Let the user actually see something!
search_box = driver.find_element_by_id("bookmakers_select") #find drop down box

time.sleep(0.25) # Let the user actually see something!

search_box_html = search_box.get_attribute('innerHTML')
search_box_list = []

while True:
    try:
        search_box_list.append(search_box_html[search_box_html.index('<option>')+8:search_box_html.index('</option>')])
        search_box_html = search_box_html[search_box_html.index('</'):]
        search_box_html = search_box_html[search_box_html.index('<o'):]
    except:
        break
        
search_box_list = search_box_list[1:]  #removes the 'all' group       
        
t = str(time.time())

with open('AllBookmakers' + t[:t.index('.')] + ".csv", 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Rating','Sport','Date','Time','Event','Outcome','Market','Bookmaker','Back','Lay','Exchange'])
    while len(search_box_list)>=1:
        time.sleep(0.25)
        search_box.send_keys(search_box_list[0]) #choose bookmaker
        driver.find_element_by_id("select_button").click() #search
        search_box_list = search_box_list[1:] #remove bookmaker from list so not repeated
        while driver.find_element_by_id("data_table_next").get_attribute('class')=='paginate_button next':
            tablehtml = driver.find_element_by_id('data_table').get_attribute('innerHTML')
            tablehtml = tablehtml[tablehtml.index('<tbody>'):]
            while True:
                try:
                    tablehtml = tablehtml[tablehtml.index('<td>'):]
                    Rating = tablehtml[tablehtml.index('">')+2:tablehtml.index("</")]
                    tablehtml = tablehtml[tablehtml.index('</td>'):]
                    tablehtml = tablehtml[tablehtml.index('<td>'):]
                    Sport = tablehtml[tablehtml.index('img/')+4:tablehtml.index(".png")]
                    tablehtml = tablehtml[tablehtml.index('</td>'):]
                    tablehtml = tablehtml[tablehtml.index('<td>'):]
                    Date = tablehtml[tablehtml.index('d>')+2:tablehtml.index("<br")]
                    Time = tablehtml[tablehtml.index('r>')+2:tablehtml.index("</")]
                    tablehtml = tablehtml[tablehtml.index('</td>'):]
                    tablehtml = tablehtml[tablehtml.index('<td>'):]
                    if tablehtml.index('<br>') < tablehtml.index('</td>'):
                        Event = tablehtml[tablehtml.index('d>')+2:tablehtml.index("<br>")] + " Vs " +  tablehtml[tablehtml.index('<br>')+4:tablehtml.index("</")]
                    else:
                        Event = tablehtml[tablehtml.index('d>')+2:tablehtml.index("</")]
                    tablehtml = tablehtml[tablehtml.index('</td>'):]
                    tablehtml = tablehtml[tablehtml.index('<td>'):]
                    if tablehtml.index('<br>') < tablehtml.index('</td>'):
                        Outcome = tablehtml[tablehtml.index('d>')+2:tablehtml.index("<br>")] + tablehtml[tablehtml.index('<br>')+4:tablehtml.index("</")]
                    else:
                        Outcome = tablehtml[tablehtml.index('d>')+2:tablehtml.index("</")]
                    tablehtml = tablehtml[tablehtml.index('</td>'):]
                    tablehtml = tablehtml[tablehtml.index('<td>'):]
                    if tablehtml.index('<br>') < tablehtml.index('</td>'):
                        Market = tablehtml[tablehtml.index('d>')+2:tablehtml.index("<br>")] + tablehtml[tablehtml.index('<br>')+4:tablehtml.index("</")]
                    else:
                        Market = tablehtml[tablehtml.index('d>')+2:tablehtml.index("</")]
                    tablehtml = tablehtml[tablehtml.index('</td>'):]
                    tablehtml = tablehtml[tablehtml.index('<td>'):]        
                    Bookmaker = tablehtml[tablehtml.index('logos/')+6:tablehtml.index(".png")]
                    tablehtml = tablehtml[tablehtml.index('</td>'):]
                    tablehtml = tablehtml[tablehtml.index('<td'):] 
                    Back = tablehtml[tablehtml.index('</span>')-4:tablehtml.index("</span>")]
                    tablehtml = tablehtml[tablehtml.index('</td>'):]
                    tablehtml = tablehtml[tablehtml.index('<td>'):]
                    Lay = tablehtml[tablehtml.index('</span>')-4:tablehtml.index("</span>")]
                    tablehtml = tablehtml[tablehtml.index('</td>'):]
                    tablehtml = tablehtml[tablehtml.index('<td>'):]
                    Exchange = tablehtml[tablehtml.index('logos/')+6:tablehtml.index(".png")]
                    spamwriter.writerow([Rating,Sport,Date,Time,Event,Outcome,Market,Bookmaker,Back,Lay,Exchange])
                    tablehtml = tablehtml[tablehtml.index('<tr'):]
                except:
                    break
            time.sleep(0.25)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element_by_id("data_table_next").click() #next page
            time.sleep(0.25)
        tablehtml = driver.find_element_by_id('data_table').get_attribute('innerHTML')
        tablehtml = tablehtml[tablehtml.index('<tbody>'):]
        while True:
            try:
                tablehtml = tablehtml[tablehtml.index('<td>'):]
                Rating = tablehtml[tablehtml.index('">')+2:tablehtml.index("</")]
                tablehtml = tablehtml[tablehtml.index('</td>'):]
                tablehtml = tablehtml[tablehtml.index('<td>'):]
                Sport = tablehtml[tablehtml.index('img/')+4:tablehtml.index(".png")]
                tablehtml = tablehtml[tablehtml.index('</td>'):]
                tablehtml = tablehtml[tablehtml.index('<td>'):]
                Date = tablehtml[tablehtml.index('d>')+2:tablehtml.index("<br")]
                Time = tablehtml[tablehtml.index('r>')+2:tablehtml.index("</")]
                tablehtml = tablehtml[tablehtml.index('</td>'):]
                tablehtml = tablehtml[tablehtml.index('<td>'):]
                if tablehtml.index('<br>') < tablehtml.index('</td>'):
                    Event = tablehtml[tablehtml.index('d>')+2:tablehtml.index("<br>")] + " Vs " +  tablehtml[tablehtml.index('<br>')+4:tablehtml.index("</")]
                else:
                    Event = tablehtml[tablehtml.index('d>')+2:tablehtml.index("</")]
                tablehtml = tablehtml[tablehtml.index('</td>'):]
                tablehtml = tablehtml[tablehtml.index('<td>'):]
                if tablehtml.index('<br>') < tablehtml.index('</td>'):
                    Outcome = tablehtml[tablehtml.index('d>')+2:tablehtml.index("<br>")] + tablehtml[tablehtml.index('<br>')+4:tablehtml.index("</")]
                else:
                    Outcome = tablehtml[tablehtml.index('d>')+2:tablehtml.index("</")]
                tablehtml = tablehtml[tablehtml.index('</td>'):]
                tablehtml = tablehtml[tablehtml.index('<td>'):]
                if tablehtml.index('<br>') < tablehtml.index('</td>'):
                    Market = tablehtml[tablehtml.index('d>')+2:tablehtml.index("<br>")] + tablehtml[tablehtml.index('<br>')+4:tablehtml.index("</")]
                else:
                    Market = tablehtml[tablehtml.index('d>')+2:tablehtml.index("</")]
                tablehtml = tablehtml[tablehtml.index('</td>'):]
                tablehtml = tablehtml[tablehtml.index('<td>'):]        
                Bookmaker = tablehtml[tablehtml.index('logos/')+6:tablehtml.index(".png")]
                tablehtml = tablehtml[tablehtml.index('</td>'):]
                tablehtml = tablehtml[tablehtml.index('<td'):] 
                Back = tablehtml[tablehtml.index('</span>')-4:tablehtml.index("</span>")]
                tablehtml = tablehtml[tablehtml.index('</td>'):]
                tablehtml = tablehtml[tablehtml.index('<td>'):]
                Lay = tablehtml[tablehtml.index('</span>')-4:tablehtml.index("</span>")]
                tablehtml = tablehtml[tablehtml.index('</td>'):]
                tablehtml = tablehtml[tablehtml.index('<td>'):]
                Exchange = tablehtml[tablehtml.index('logos/')+6:tablehtml.index(".png")]
                spamwriter.writerow([Rating,Sport,Date,Time,Event,Outcome,Market,Bookmaker,Back,Lay,Exchange])
                tablehtml = tablehtml[tablehtml.index('<tr'):]
            except:
                while driver.find_element_by_id("data_table_previous").get_attribute('class')=='paginate_button previous':
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    driver.find_element_by_id("data_table_previous").click()
                    time.sleep(0.25) #doesn't auto return to page 1
                break
                
print('done')
time.sleep(0.25) 
driver.quit() #closes window
print('Time Elapsed: ' + str(time.time() - start) + 's')
