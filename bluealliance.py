from __future__ import print_function
import time
import json
import tbaapiv3client
import awardtypes
from tbaapiv3client.models import event
from tbaapiv3client.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
with open('../theBlueAllianceApiKey.txt') as keyfile:

    actual_key = keyfile.readline()[:-1] # strip newline

    configuration = tbaapiv3client.Configuration(
        host = "https://www.thebluealliance.com/api/v3",
        api_key = {
            'X-TBA-Auth-Key': actual_key
        }
    )

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

api_response = None
test_award = None

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.TeamApi(api_client)
    event_api_instance = tbaapiv3client.EventApi(api_client)

    # TODO: get all event keys from teams (this is below and works), then iterate over events;
    # in each event, find the fraction of teams who won impact/EI and the fraction
    # who won a MCI award and multiply these two to find the predicted fraction of teams to win both.
    # Then, see if the EI and Impact winners actually did win any MCI awards, and add that to an average.
    # This will give a predicted and actual fraction.
    """
    event_keys = set()
    for team_number in range(3):
        print(f"Getting event keys from team number {team_number}")
        try:
            team_awards = api_instance.get_team_awards(team_key=f"frc{team_number}")
            for award in team_awards:
                print(f"found event key {award.event_key}")
                event_keys.add(award.event_key)

        except ApiException as e:
            print(f"could not obtain award list for team {team_number}")

            
    print(f"event_keys: {event_keys}")
    """

    event_keys = set()
    for year in range(2016, 2025):
        events = event_api_instance.get_events_by_year_simple(year)
        for event_to_get_key_from in events:
            event_keys.add(event_to_get_key_from.key)

    print(f"event_keys: {event_keys}")

    mci_awards = awardtypes.mci_awards
    great_awards = awardtypes.great_awards
    other_awards = awardtypes.other_awards

    # compare the average fraction of teams who won both
    # with
    # the average fraction of teams expecetd to win both
    fractions_who_actually_won_both = []
    expected_fractions_to_win_both = []
    num_events_considered = 0

    # TODO: for each event:

    for event_key in event_keys:
        num_events_considered += 1

        this_event_awards = event_api_instance.get_event_awards(event_key)
        # pprint(this_event_awards)
        # list of award names so we can figure out what kind of awards these are
        num_teams_here = len(event_api_instance.get_event_teams_simple(event_key))


        if num_teams_here == 0: # occassionally true
            continue

        # the teams to win a type of award at this event
        mcis_at_this_event = set()
        greats_at_this_event = set()
        others_at_this_event = set()

        # figure out which awards went to which teams
        for award in this_event_awards:

            # we don't know if this is a MCI or great or other award, so let's figure it out
            if not award.name in mci_awards + great_awards + other_awards:
                user_response = input(f"\nif {award.name} is an awesome award, type a; if it's a mci award, type r: ")
                # other awards only exists so we don't prompt unnecessarily
                # NOTE: there's a lot of data here- we can find the probabilities of any award given any other award
                # e.g. we can find how much mci awards are related to ta awards etc... we can do a whole graph possibly
                # TODO: figure out the probability of each award given each other award (makes a matrix)
                # and figure out the fraction getting impact given robot game, as a function of getting impact. make a dot graph with one dot per event.
                if user_response == "a":
                    great_awards.append(award.name)
                elif user_response == "r":
                    mci_awards.append(award.name)
                else:
                    other_awards.append(award.name)

                with open("awardtypes.py", "w") as awardtypes:
                    awardtypes.write(f"great_awards = {great_awards}; mci_awards = {mci_awards}; other_awards = {other_awards}")

            recipient_teams_of_this_award = [recipient_being_added.team_key for recipient_being_added in award.recipient_list]
            print(f"{award.name} recipient teams: {recipient_teams_of_this_award}")

            if award.name in mci_awards:
                mcis_at_this_event = mcis_at_this_event.union(recipient_teams_of_this_award)
            elif award.name in great_awards:
                greats_at_this_event = greats_at_this_event.union(recipient_teams_of_this_award)
            else:
                others_at_this_event = others_at_this_event.union(recipient_teams_of_this_award)
                

        print(f"there were {num_teams_here} teams at {event_key}")
        print(f"{len(mcis_at_this_event)} mcis were awarded; {len(greats_at_this_event)} great awards were awarded; and {len(others_at_this_event)} other awards were awarded")

        mci_fraction = len(mcis_at_this_event) / num_teams_here
        greats_fraction = len(greats_at_this_event) / num_teams_here

        expected_both_fraction = mci_fraction * greats_fraction
        expected_fractions_to_win_both.append(expected_both_fraction)


        teams_who_won_both = mcis_at_this_event.intersection(greats_at_this_event)
        actual_fraction_to_win_both = len(teams_who_won_both)/num_teams_here
        fractions_who_actually_won_both.append(len(teams_who_won_both))

        print(f"the teams who won both an mci and a great award are: {teams_who_won_both}")
        print(f"the actual fraction of teams to recieve both is {actual_fraction_to_win_both}")
        print(f"the expected fraction was {expected_both_fraction}")
    
    average_actual_both = sum(fractions_who_actually_won_both) / len(fractions_who_actually_won_both)
    average_expected_both = sum(expected_fractions_to_win_both) / len(expected_fractions_to_win_both)
    print(f"FINAL RESULTS!! average actual both: {average_actual_both}; average expected both: {average_expected_both}")
