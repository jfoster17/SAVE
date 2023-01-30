import datacommons_pandas as dc
import ipywidgets as widgets

class GetDataButton(object):
    
    def __init__(self, parent):
        self.parent = parent
        self.button = widgets.Button(
                            description='Get Data',
                            disabled=False,
                            button_style='',
                            tooltip='Get Data',
                            icon='table' 
                        )
        self.button.on_click(self.button_pressed)
        self.stat_vars = {}
    
    def get_data_commons(self):
        if self.stat_vars == []:
            print("No variables requested, nothing to be done...")
            return
        self.button.disabled=True
        self.button.icon = 'spinner'
        try:
            stat_vars_to_get = []
            for x in self.stat_vars.values():
                stat_vars_to_get.extend(x)
            place_ids = list(self.parent.glue_data_object['place'])
            new_data = dc.build_multivariate_dataframe(place_ids, stat_vars_to_get)
            self.parent.update_data_collection(new_data)
        except Exception as e: 
            print(f"{e}")
        self.button.disabled=False
        self.button.icon = 'table'
    
    def button_pressed(self, *args):
        self.get_data_commons()


class InputWidget(object):
    
    def __init__(self, options_dict, description, button):
        self.layout=widgets.Layout(width='450px', height='200px')
        self.options_dict = options_dict
        self.description = description

        self.input_widget = widgets.SelectMultiple(
                        options=options_dict.keys(),
                        value=[],
                        rows=10,
                        description=self.description,
                        disabled=False,
                        layout=self.layout
                        )
        self.data_button = button
        
    def on_value_change(self, change):
        self.data_button.stat_vars[change['owner'].description] = [self.options_dict[x] for x in change['new']]

class DataCommonsChoices(object):
    
    def __init__(self, glue_data_object=None):
        
        self.glue_data_object = glue_data_object
        self.data_button = GetDataButton(self)
        self.input_widgets = self.get_input_widgets()
        self.input_widget_names = [x.description for x in self.input_widgets]
        self.stat_vars = dict.fromkeys(self.input_widget_names, [])
        self.accordion = widgets.Accordion(children=[x.input_widget for x in self.input_widgets])
        # This works in ipywidgets 8           titles=self.input_widget_names)
        # Otherwise we do below
        for i,title in enumerate(self.input_widget_names):
            self.accordion.set_title(i,title)
        for x in self.input_widgets:
            x.input_widget.observe(x.on_value_change, names='value')
        # We might need this only for ipywidgets 7
        self.accordion.selected_index = None

    def update_data_collection(self, new_data, glue_data_object=None):
        if not glue_data_object:
            glue_data_object = self.glue_data_object
        temp_data = glue_data_object.to_dataframe().set_index('place').drop(['Pixel Axis 0 [x]'],axis=1)
        cols_to_use = new_data.columns.difference(temp_data.columns)
        new_data = temp_data.merge(new_data[cols_to_use], left_index=True, right_index=True)
        for col in cols_to_use:
            glue_data_object.add_component(new_data[col],label=col)

    def get_input_widgets(self):
        household_income_options = {'Count of Household: 10,000 USD or Less':'Count_Household_IncomeOfUpto10000USDollar',
                    'Count of Household: 10,000 - 14,999 USD':'Count_Household_IncomeOf10000To14999USDollar',
                    'Count of Household: 15,000 - 19,999 USD':'Count_Household_IncomeOf15000To19999USDollar',
                    'Count of Household: 20,000 - 24,999 USD':'Count_Household_IncomeOf20000To24999USDollar',
                    'Count of Household: 25,000 - 29,999 USD':'Count_Household_IncomeOf25000To29999USDollar',
                    'Count of Household: 30,000 - 34,999 USD':'Count_Household_IncomeOf30000To34999USDollar',
                    'Count of Household: 35,000 - 39,999 USD':'Count_Household_IncomeOf35000To39999USDollar',
                    'Count of Household: 40,000 - 44,999 USD':'Count_Household_IncomeOf40000To44999USDollar',
                    'Count of Household: 45,000 - 49,999 USD':'Count_Household_IncomeOf45000To49999USDollar',
                    'Count of Household: 50,000 - 59,999 USD':'Count_Household_IncomeOf50000To59999USDollar',
                    'Count of Household: 60,000 - 74,999 USD':'Count_Household_IncomeOf60000To74999USDollar',
                    'Count of Household: 75,000 - 99,999 USD':'Count_Household_IncomeOf75000To99999USDollar',
                    'Count of Household: 100,000 - 124,999 USD':'Count_Household_IncomeOf100000To124999USDollar',
                    'Count of Household: 125,000 - 149,999 USD':'Count_Household_IncomeOf125000To149999USDollar',
                    'Count of Household: 150,000 - 199,999 USD':'Count_Household_IncomeOf150000To199999USDollar',
                    'Count of Household: 200,000 USD or More':'Count_Household_IncomeOf200000OrMoreUSDollar',
                           }


        health_options = {'Prevalence: Sleep Less Than 7 Hours':'Percent_Person_SleepLessThan7Hours',
                          'Prevalence: Obesity':'Percent_Person_Obesity',
                          'Prevalence: Binge Drinking':'Percent_Person_BingeDrinking',
                          'Prevalence: Physical Inactivity':'Percent_Person_PhysicalInactivity',
                          'Prevalence: Smoking':'Percent_Person_Smoking',
                          'Prevalence: High Cholesterol':'Percent_Person_WithHighCholesterol',
                          'Prevalence: High Blood Pressure':'Percent_Person_WithHighBloodPressure',
                          'Prevalence: Arthritis':'Percent_Person_WithArthritis',
                          'Prevalence: Mental Health Not Good':'Percent_Person_WithMentalHealthNotGood',
                          'Prevalence: Physical Health Not Good':'Percent_Person_WithPhysicalHealthNotGood',
                         }

        environment_options = {'Lifetime Air Toxins Cancer Risk': 'AirPollutant_Cancer_Risk',
                               'Mean Concentration: Diesel PM': 'Mean_Concentration_AirPollutant_DieselPM',
                               #'Mean Ozone Concentration': 'Mean_Concentration_AirPollutant_Ozone',
                               #'Mean PM2.5 Concentration': 'Mean_Concentration_AirPollutant_PM2.5',
                        }


        return [InputWidget(household_income_options, 'Income', self.data_button),
                InputWidget(health_options, 'Health', self.data_button),
                InputWidget(environment_options, 'Environment', self.data_button)]

if __name__ == "__main__":
    dc_widget = DataCommonsChoices()
    display(dc_widget.accordion, dc_widget.data_button.button)