import datetime
import time
import os
from pathlib import Path
import click
import pandas as pd
from PyInquirer import prompt
from pyfiglet import Figlet
from click_help_colors import HelpColorsGroup
from halo import Halo

timestr = time.strftime("%Y%m%d-%H%M%S")
spinner = Halo(text="Downloading data source(csv)", spinner="dots")

# DEFAULT URLS FOR DATASOURCE
confirmed_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
recovered_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
death_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
previous_cases_url = "https://raw.githubusercontent.com/Jcharis/covidcli/master/covidcli/data/coronavirus_dataset.csv"


def get_previous_datasets():
    previous_filepath = Path("./previous_dataset")
    return os.listdir(previous_filepath)


def get_n_melt_data(data_url, case_type):
    df = pd.read_csv(data_url)
    melted_df = df.melt(id_vars=["Province/State", "Country/Region", "Lat", "Long"])
    melted_df.rename(columns={"variable": "Date", "value": case_type}, inplace=True)
    return melted_df


def merge_data(confirm_df, recovered_df, deaths_df):
    new_df = confirm_df.join(recovered_df["Recovered"]).join(deaths_df["Deaths"])
    return new_df


confirm_df = get_n_melt_data(confirmed_cases_url, "Confirmed")
recovered_df = get_n_melt_data(recovered_cases_url, "Recovered")
deaths_df = get_n_melt_data(death_cases_url, "Deaths")


@click.group(
    cls=HelpColorsGroup, help_headers_color="yellow", help_options_color="cyan"
)
@click.version_option("0.1.4", prog_name="covid")
def main():
    """Covid CLI"""
    pass


@main.group()
def get():
    """Get Cases"""
    pass


@get.command("latest")
def get_latest():
    """Get Latest Cases"""
    click.echo(
        click.style("Accessed Time::", fg="blue") + "{}".format(datetime.datetime.now())
    )
    click.echo("===================")
    try:
        spinner.start("Merging several datasets...")
        df = merge_data(confirm_df, recovered_df, deaths_df)
        time.sleep(3)
        spinner.succeed("Merged several datasets")
        time.sleep(2)
        spinner.start("Downloading source dataset")
        df.to_csv("coronavirus_dataset.csv")
        spinner.succeed("Downloading is DONE!")
        time.sleep(3)
        total_confirmed = df["Confirmed"].sum()
        total_recovered = df["Recovered"].sum()
        total_deaths = df["Deaths"].sum()
        stat_dict = {
            "Confirmed Cases": total_confirmed,
            "Recovered Cases": total_recovered,
            "Deaths Cases": total_deaths,
        }
        spinner.succeed("Job is Finished!!")
        click.echo(stat_dict)
    except (KeyboardInterrupt, SystemExit):
        spinner.stop()


@get.command("previous")
def get_previous():
    """Get Previous Cases"""
    click.echo("===================")
    spinner.start("Get Previous Cases")
    try:
        spinner.info("Scanning previous datasets from local directory...")
        files_list = get_previous_datasets()
        previous_datasets = [
            {
                "type": "list",
                "name": "filepath",
                "message": "dataset path",
                "choices": map(lambda el: "./previous_dataset/" + el, files_list),
            }
        ]
        if len(files_list) != 0:
            dataset = prompt(previous_datasets)["filepath"]
        else:
            dataset = previous_cases_url
        spinner.info("Parsing csv data...")
        prev_df = pd.read_csv(dataset)
        total_confirmed = prev_df["Confirmed"].sum()
        total_recovered = prev_df["Recovered"].sum()
        total_deaths = prev_df["Deaths"].sum()
        stat_dict = {
            "Confirmed Cases": total_confirmed,
            "Recovered Cases": total_recovered,
            "Deaths Cases": total_deaths,
        }
        spinner.succeed("Finished!!")
        click.echo(stat_dict)
    except (KeyboardInterrupt, SystemExit):
        spinner.stop()


@get.command("status")
@click.argument("countryname")
def get_status(countryname):
    """Get Status by Country

    eg. covid get status "Ghana"
    """
    click.echo("Showing Status of Cases")
    click.echo(click.style("Country::", fg="blue") + "{}".format(countryname))
    click.echo(
        click.style("Accessed Time::", fg="blue") + "{}".format(datetime.datetime.now())
    )
    click.echo("===================")
    new_df = merge_data(confirm_df, recovered_df, deaths_df)
    single_country_df = new_df[new_df["Country/Region"] == countryname]
    total_confirmed = single_country_df["Confirmed"].sum()
    total_recovered = single_country_df["Recovered"].sum()
    total_deaths = single_country_df["Deaths"].sum()
    stat_dict = {
        "Confirmed Cases": total_confirmed,
        "Recovered Cases": total_recovered,
        "Deaths Cases": total_deaths,
    }
    click.echo(stat_dict)


@get.command("dataset")
def get_dataset():
    """Get/Download Dataset Cases"""
    click.echo("Fetching Latest Dataset of Cases")
    click.echo(
        click.style("Accessed Time::", fg="blue") + "{}".format(datetime.datetime.now())
    )
    click.echo("====================")
    current_df = merge_data(confirm_df, recovered_df, deaths_df)
    file_name = os.path.join(
        "./previous_dataset", "coronavirus_dataset_{}.csv".format(timestr)
    )
    # click.echo(current_df.tail(20))
    current_df.to_csv(file_name, index=False)
    click.secho(
        "Finished Downloading Dataset and Saved as {}".format(file_name),
        fg="white",
        bg="blue",
    )


@main.command()
@click.argument("countryname")
@click.option(
    "--cases",
    "-c",
    type=click.Choice(["confirmed", "recovered", "deaths", "previous", "latest"]),
)
def search(countryname, cases):
    """Search Cases By Country
    eg. covid search "Country name" --cases confirmed
    """
    click.echo(click.style("Searched::", fg="blue") + "{}".format(countryname))
    click.echo(
        click.style("Accessed Time::", fg="blue") + "{}".format(datetime.datetime.now())
    )
    click.echo("===================")
    df = merge_data(confirm_df, recovered_df, deaths_df)
    country_df = df[df["Country/Region"] == countryname]
    if cases == "confirmed":
        total_confirmed = country_df["Confirmed"].sum()
        click.echo(
            click.style("Accessed Time:: ", fg="blue")
            + "{}".format(datetime.datetime.now())
        )
        click.echo(
            "Total Number of {} Cases for {}::{}".format(
                cases, countryname, total_confirmed
            )
        )
    elif cases == "recovered":
        total_recovered = country_df["Recovered"].sum()
        click.echo(
            click.style("Accessed Time:: ", fg="blue")
            + "{}".format(datetime.datetime.now())
        )
        click.echo(
            "Total Number of {} Cases for {}::{}".format(
                cases, countryname, total_recovered
            )
        )
    elif cases == "deaths":
        total_deaths = country_df["Deaths"].sum()
        click.echo(
            click.style("Accessed Time:: ", fg="blue")
            + "{}".format(datetime.datetime.now())
        )
        click.echo(
            "Total Number of {} Cases for {}::{}".format(
                cases, countryname, total_deaths
            )
        )
    elif cases == "previous":
        prev_df = pd.read_csv(previous_cases_url)
        prev_country_df = prev_df[prev_df["Country/Region"] == countryname]
        click.echo("Showing Previous Data")
        click.echo(prev_country_df)
    elif cases == "latest":
        current_df = merge_data(confirm_df, recovered_df, deaths_df)
        current_country_df = current_df[current_df["Country/Region"] == countryname]
        click.echo("Showing Latest Data")
        click.echo(current_country_df)
    else:
        click.echo(country_df)


@main.command()
@click.argument("cases", type=click.Choice(["confirmed", "recovered", "deaths", "all"]))
def show(cases):
    """Show Cases Confirmed|Recovered|Death"""
    click.secho("Showing:: {} Cases".format(cases), bg="blue")
    click.echo("=============")
    if cases == "confirmed":
        click.secho(
            "Number of Confirmed Cases:: {}".format(confirm_df["Confirmed"].sum())
        )
        click.echo(confirm_df)
    elif cases == "recovered":
        click.secho(
            "Number of Confirmed Cases:: {}".format(recovered_df["Recovered"].sum())
        )
        click.echo(recovered_df)
    elif cases == "deaths":
        click.secho("Number of Confirmed Cases:: {}".format(deaths_df["Deaths"].sum()))
        click.echo(deaths_df)
    elif cases == "all":
        df = merge_data(confirm_df, recovered_df, deaths_df)
        click.echo(df.tail(20))


@main.command()
def info():
    """Info About Cli"""
    click.echo("================")
    f = Figlet(font="slant")
    click.echo(f.renderText("Covid-CLI"))
