
from drafter import *
from dataclasses import dataclass


# ==========================================
# WEBSITE INFORMATION
# ==========================================

set_website_title("Badminton Performance Tracker")

set_site_information(
    "Danny Nguyen",
    "A website that helps badminton players record matches, "
    "analyze statistics, and improve their performance.",
    "Drafter Documentation, CISC 106 course materials, "
    "and ChatGPT for coding assistance.",
    "Badminton Performance Tracker Final Project Mockup "
    "and Implementing Requirements.",
    [
        "https://github.com/dannyn-68/badminton-performance-tracker",
        "https://drafter-edu.github.io/drafter/"
    ]
)

set_website_style("none")


# ==========================================
# WEBSITE DECORATION
# ==========================================

# Advanced technique: CSS styling.
# CSS controls the appearance of HTML components.
# add_website_css applies these rules to every page.
# A class selector such as .hero styles components
# that have classes="hero".
# CSS Grid creates responsive layouts that adjust
# to different screen sizes.
# The :hover selector changes button appearance
# when the mouse moves over a button.

add_website_css("""
    body {
        background-color: #f1f5f9;
        font-family: Arial, Helvetica, sans-serif;
        color: #102a43;
        margin: 0;
        padding: 20px;
        line-height: 1.6;
    }

    h1 {
        font-size: 34px;
        font-weight: 800;
        margin: 10px 0 16px;
        line-height: 1.2;
    }

    h2 {
        font-size: 23px;
        color: #102a43;
        margin: 10px 0 16px;
    }

    h3 {
        font-size: 18px;
        color: #15803d;
    }

    button {
        background-color: #16a34a;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 13px 22px;
        font-size: 15px;
        font-weight: bold;
        margin: 6px 4px;
        cursor: pointer;
        transition: 0.2s;
    }

    button:hover {
        background-color: #15803d;
        transform: translateY(-2px);
        box-shadow: 0 5px 12px #b6d8c0;
    }

    input, select, textarea {
        background-color: white;
        color: #102a43;
        border: 2px solid #cbd5e1;
        border-radius: 10px;
        padding: 12px;
        margin: 6px 0 16px;
        font-size: 16px;
        width: 100%;
        box-sizing: border-box;
    }

    input:focus, select:focus, textarea:focus {
        border-color: #16a34a;
        outline: none;
        box-shadow: 0 0 0 3px #dcfce7;
    }

    .dashboard {
        max-width: 1050px;
        margin: 0 auto;
    }

    .topbar {
        background-color: #102a43;
        color: white;
        border-radius: 14px;
        padding: 16px 24px;
        margin-bottom: 18px;
        font-weight: bold;
        letter-spacing: 2px;
        font-size: 14px;
    }

    .hero {
        background: linear-gradient(
            135deg, #102a43, #14532d
        );
        color: white;
        border-radius: 22px;
        padding: 38px;
        margin-bottom: 24px;
        box-shadow: 0 8px 20px #cbd5e1;
        border-bottom: 5px solid #86efac;
    }

    .hero h1 {
        color: white;
        font-size: 38px;
        margin-bottom: 14px;
    }

    .hero h2 {
        color: #dcfce7;
    }

    .hero button {
        background-color: #86efac;
        color: #14532d;
        margin-top: 20px;
    }

    .hero button:hover {
        background-color: #bbf7d0;
    }

    .eyebrow {
        color: #86efac;
        font-size: 13px;
        font-weight: bold;
        letter-spacing: 3px;
        margin-bottom: 12px;
    }

    .hero-description {
        color: #dcfce7;
        font-size: 17px;
        margin: 12px 0;
    }

    .section-title {
        font-size: 24px;
        font-weight: bold;
        color: #102a43;
        margin: 26px 0 14px;
    }

    .section-card {
        background-color: white;
        border-radius: 16px;
        padding: 24px;
        margin: 18px 0;
        box-shadow: 0 4px 14px #dbe4ed;
        border-left: 5px solid #22c55e;
    }

    .stat-grid {
        display: grid;
        grid-template-columns:
            repeat(auto-fit, minmax(150px, 1fr));
        gap: 16px;
        margin: 20px 0;
    }

    .stat-card {
        background-color: white;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 22px;
        text-align: center;
        box-shadow: 0 4px 12px #dbe4ed;
    }

    .stat-icon {
        font-size: 28px;
        margin-bottom: 8px;
    }

    .stat-value {
        font-size: 30px;
        font-weight: bold;
        color: #15803d;
        margin: 6px 0;
        overflow-wrap: anywhere;
    }

    .stat-label {
        font-size: 14px;
        color: #64748b;
        font-weight: bold;
    }

    .navigation {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin: 20px 0;
    }

    .secondary-button {
        background-color: #102a43;
    }

    .secondary-button:hover {
        background-color: #243b53;
    }

    .match-card {
        background-color: white;
        border-radius: 18px;
        padding: 24px;
        margin: 18px 0;
        border-left: 6px solid #16a34a;
        box-shadow: 0 4px 12px #dbe4ed;
    }

    .match-label {
        color: #15803d;
        font-weight: bold;
        font-size: 13px;
        letter-spacing: 2px;
    }

    .progress-track {
        background-color: #e2e8f0;
        height: 16px;
        border-radius: 20px;
        overflow: hidden;
        margin: 12px 0 20px;
    }

    .progress-fill {
        background: linear-gradient(
            90deg, #15803d, #86efac
        );
        height: 16px;
        border-radius: 20px;
    }

    .success-card {
        background-color: #f0fdf4;
        border: 2px solid #86efac;
        border-radius: 18px;
        padding: 28px;
        margin: 20px 0;
        text-align: center;
    }

    .error-card {
        background-color: #fef2f2;
        border: 2px solid #fca5a5;
        border-radius: 18px;
        padding: 28px;
        margin: 20px 0;
    }

    .error-card h1 {
        color: #b91c1c;
    }

    .empty-card {
        background-color: white;
        border: 2px dashed #cbd5e1;
        border-radius: 18px;
        padding: 35px;
        margin: 20px 0;
        text-align: center;
    }

    .field-label {
        font-weight: bold;
        color: #334155;
        margin-top: 10px;
    }

    .tip-card {
        background-color: #ecfdf5;
        border: 1px solid #bbf7d0;
        border-radius: 14px;
        padding: 20px;
        margin: 20px 0;
        color: #14532d;
    }

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 13px;
        padding: 24px;
        margin-top: 30px;
        border-top: 1px solid #cbd5e1;
    }

    @media (max-width: 600px) {
        body {
            padding: 10px;
        }

        .hero {
            padding: 24px;
        }

        .hero h1 {
            font-size: 28px;
        }

        .stat-grid {
            grid-template-columns:
                repeat(2, minmax(0, 1fr));
        }

        .stat-value {
            font-size: 22px;
        }

        .section-card {
            padding: 18px;
        }
    }
""")


# ==========================================
# DATACLASSES
# ==========================================

@dataclass
class Match:
    opponent: str
    points_won: int
    total_points: int
    errors: int
    total_smashes: int
    successful_smashes: int
    total_serves: int
    successful_serves: int


@dataclass
class State:
    matches: list[Match]
    player_name: str
    goal: str
    favorite_shot: str


# ==========================================
# HELPER FUNCTIONS
# ==========================================

# These helper functions create reusable website
# components so that every page has a consistent
# design without repeating the same code.


def topbar() -> Div:
    return Div(
        "🏸 BADMINTON PERFORMANCE TRACKER",
        classes="topbar"
    )


def footer() -> Div:
    return Div(
        "Badminton Performance Tracker",
        Div("Train. Track. Improve."),
        Div("Designed by Danny Nguyen | 2026"),
        classes="footer"
    )


def stat_card(
    icon: str,
    value: str,
    label: str
) -> Div:

    return Div(
        Div(icon, classes="stat-icon"),
        Div(value, classes="stat-value"),
        Div(label, classes="stat-label"),
        classes="stat-card"
    )


def progress_bar(rate: float) -> Div:

    # Advanced technique: Dynamic CSS styling.
    # The percentage is converted to a string and
    # used as the width of the colored progress bar.
    # For example, a rate of 75 creates a bar that
    # fills 75 percent of its container.

    return Div(
        Div(
            "",
            classes="progress-fill",
            style_width=str(rate) + "%"
        ),
        classes="progress-track"
    )


def match_error(state: State, message: str) -> Page:

    return Page(state, [
        Div(
            topbar(),

            Div(
                Header("⚠ Invalid Input"),
                Div(message),

                Button("Try Again", record_match),

                Button(
                    "Back to Home",
                    index,
                    classes="secondary-button"
                ),

                classes="error-card"
            ),

            footer(),

            classes="dashboard"
        )
    ])


# ==========================================
# ROUTE 1: HOME PAGE
# ==========================================

@route
def index(state: State) -> Page:

    return Page(state, [
        Div(

            topbar(),

            # Hero banner

            Div(
                Div(
                    "TRAIN. TRACK. IMPROVE.",
                    classes="eyebrow"
                ),

                Header("🏸 Elevate Your Game."),

                Header(
                    "Welcome, " + state.player_name + "!",
                    2
                ),

                Div(
                    "Every match is a chance to get better. "
                    "Track your performance, discover your "
                    "strengths, and reach your goals.",
                    classes="hero-description"
                ),

                Button("+ Record a Match", record_match),

                classes="hero"
            ),

            # Performance overview

            Div(
                "Your Performance Overview",
                classes="section-title"
            ),

            Div(

                stat_card(
                    "🏆",
                    str(len(state.matches)),
                    "Matches Recorded"
                ),

                stat_card(
                    "⚡",
                    state.favorite_shot,
                    "Favorite Shot"
                ),

                stat_card(
                    "🎯",
                    "Active",
                    "Training Status"
                ),

                classes="stat-grid"
            ),

            # Personal training goal

            Div(
                Header("🎯 Your Training Goal", 2),

                Div(state.goal),

                Button("Update Goal", profile),

                classes="section-card"
            ),

            # Website navigation

            Div(
                "Explore Your Dashboard",
                classes="section-title"
            ),

            Div(

                Div(
                    Header("🏸 Record Match", 2),

                    Div(
                        "Log your points, errors, "
                        "smashes, and serves."
                    ),

                    Button("Record Match", record_match),

                    classes="section-card"
                ),

                Div(
                    Header("📋 Match History", 2),

                    Div(
                        "Review your previously "
                        "recorded matches."
                    ),

                    Button("Match History", match_history),

                    classes="section-card"
                ),

                Div(
                    Header("📊 Statistics", 2),

                    Div(
                        "Analyze your success rates "
                        "and overall performance."
                    ),

                    Button("View Statistics", statistics),

                    classes="section-card"
                ),

                Div(
                    Header("👤 My Profile", 2),

                    Div(
                        "Personalize your name, "
                        "goals, and favorite shot."
                    ),

                    Button("My Profile", profile),

                    classes="section-card"
                ),

                classes="stat-grid"
            ),

            Div(
                Header("💡 Training Tip", 2),

                Div(
                    "Focus on consistency before power. "
                    "Reducing unforced errors can make "
                    "a big difference in your matches."
                ),

                classes="tip-card"
            ),

            footer(),

            classes="dashboard"
        )
    ])


# ==========================================
# ROUTE 2: RECORD MATCH PAGE
# ==========================================

@route
def record_match(state: State) -> Page:

    return Page(state, [
        Div(

            topbar(),

            Div(
                Div(
                    "MATCH TRACKING",
                    classes="eyebrow"
                ),

                Header("🏸 Record a Match"),

                Div(
                    "Log your performance. "
                    "Learn from every game.",
                    classes="hero-description"
                ),

                classes="hero"
            ),

            # Match information

            Div(
                Header("👥 Match Information", 2),

                Div(
                    "Opponent Name",
                    classes="field-label"
                ),

                TextBox("opponent", ""),

                classes="section-card"
            ),

            # Point statistics

            Div(
                Header("🏆 Point Statistics", 2),

                Div(
                    "Points Won",
                    classes="field-label"
                ),

                TextBox("points_won", "0"),

                Div(
                    "Total Points Played",
                    classes="field-label"
                ),

                TextBox("total_points", "0"),

                Div(
                    "Errors",
                    classes="field-label"
                ),

                TextBox("errors", "0"),

                classes="section-card"
            ),

            # Smash statistics

            Div(
                Header("⚡ Smash Statistics", 2),

                Div(
                    "Total Smashes",
                    classes="field-label"
                ),

                TextBox("total_smashes", "0"),

                Div(
                    "Successful Smashes",
                    classes="field-label"
                ),

                TextBox("successful_smashes", "0"),

                classes="section-card"
            ),

            # Serve statistics

            Div(
                Header("🎯 Serve Statistics", 2),

                Div(
                    "Total Serves",
                    classes="field-label"
                ),

                TextBox("total_serves", "0"),

                Div(
                    "Successful Serves",
                    classes="field-label"
                ),

                TextBox("successful_serves", "0"),

                classes="section-card"
            ),

            Div(
                "💡 Enter whole numbers for all statistics. "
                "Total points must be greater than zero.",
                classes="tip-card"
            ),

            Div(

                Button("✓ Save Match", save_match),

                Button(
                    "← Back to Home",
                    index,
                    classes="secondary-button"
                ),

                classes="navigation"
            ),

            footer(),

            classes="dashboard"
        )
    ])


# ==========================================
# ROUTE 3: SAVE MATCH
# ==========================================

@route
def save_match(
    state: State,
    opponent: str,
    points_won: str,
    total_points: str,
    errors: str,
    total_smashes: str,
    successful_smashes: str,
    total_serves: str,
    successful_serves: str
) -> Page:

    # Advanced technique: Exception handling.
    # TextBox inputs are strings.
    # The try block attempts to convert the strings
    # into integers using int().
    # If a conversion fails, Python raises ValueError.
    # The except block displays an error message
    # instead of allowing the website to crash.
    # Separate integer variables prevent type errors.

    try:
        won = int(points_won)
        total = int(total_points)
        error_count = int(errors)
        smashes = int(total_smashes)
        good_smashes = int(successful_smashes)
        serves = int(total_serves)
        good_serves = int(successful_serves)

    except ValueError:

        return match_error(
            state,
            "Please enter whole numbers for all statistics."
        )

    # Meaningful if statement 1:
    # Make sure the opponent's name is provided.

    if opponent.strip() == "":

        return match_error(
            state,
            "Please enter your opponent's name."
        )

    # Meaningful if statement 2:
    # Check that the point statistics are valid.

    if total <= 0 or won < 0 or won > total:

        return match_error(
            state,
            "Points won must be between 0 and total "
            "points. Total points must be greater than zero."
        )

    # Meaningful if statement 3:
    # Prevent negative error counts.

    if error_count < 0:

        return match_error(
            state,
            "The number of errors cannot be negative."
        )

    # Meaningful if statement 4:
    # Validate smash statistics.

    if smashes < 0 or good_smashes < 0 or good_smashes > smashes:

        return match_error(
            state,
            "Successful smashes must be between "
            "0 and total smashes."
        )

    # Meaningful if statement 5:
    # Validate serve statistics.

    if serves < 0 or good_serves < 0 or good_serves > serves:

        return match_error(
            state,
            "Successful serves must be between "
            "0 and total serves."
        )

    # Create a new Match dataclass instance.

    new_match = Match(
        opponent.strip(),
        won,
        total,
        error_count,
        smashes,
        good_smashes,
        serves,
        good_serves
    )

    # Meaningfully modify State field 1.

    state.matches.append(new_match)

    return Page(state, [
        Div(

            topbar(),

            Div(
                Div("✓", classes="stat-icon"),

                Header("Match Saved Successfully!"),

                Div(
                    "Your match against " + opponent
                    + " has been recorded."
                ),

                Div(
                    "Keep tracking your matches "
                    "and improving your skills."
                ),

                classes="success-card"
            ),

            Div(

                stat_card(
                    "🏆",
                    str(won) + "/" + str(total),
                    "Points Won"
                ),

                stat_card(
                    "⚡",
                    str(good_smashes) + "/" + str(smashes),
                    "Successful Smashes"
                ),

                stat_card(
                    "🎯",
                    str(good_serves) + "/" + str(serves),
                    "Successful Serves"
                ),

                classes="stat-grid"
            ),

            Div(

                Button(
                    "+ Record Another Match",
                    record_match
                ),

                Button(
                    "📋 Match History",
                    match_history
                ),

                Button(
                    "📊 View Statistics",
                    statistics
                ),

                Button(
                    "← Back to Home",
                    index,
                    classes="secondary-button"
                ),

                classes="navigation"
            ),

            footer(),

            classes="dashboard"
        )
    ])


# ==========================================
# ROUTE 4: MATCH HISTORY PAGE
# ==========================================

@route
def match_history(state: State) -> Page:

    # The content list contains Div components.
    # Additional match cards are appended below.

    content: list[Div] = [

        topbar(),

        Div(
            Div(
                "YOUR MATCH JOURNEY",
                classes="eyebrow"
            ),

            Header("📋 Match History"),

            Div(
                "Review your previous matches "
                "and track your progress.",
                classes="hero-description"
            ),

            classes="hero"
        ),

        Div(
            stat_card(
                "🏆",
                str(len(state.matches)),
                "Total Matches Recorded"
            ),

            classes="stat-grid"
        )
    ]

    # Display a helpful message when there are
    # no saved matches.

    if len(state.matches) == 0:

        content.append(
            Div(
                Div("🏸", classes="stat-icon"),

                Header("No Matches Yet", 2),

                Div(
                    "Your badminton journey starts here. "
                    "Record your first match to begin."
                ),

                Button(
                    "Record Your First Match",
                    record_match
                ),

                classes="empty-card"
            )
        )

    match_number = 1

    # Meaningful loop:
    # Iterate through the list of Match instances
    # stored in the State dataclass.
    # Display each match in its own styled card.

    for match in state.matches:

        content.append(
            Div(

                Div(
                    "MATCH #" + str(match_number),
                    classes="match-label"
                ),

                Header(
                    "🏸 vs. " + match.opponent,
                    2
                ),

                Div(

                    stat_card(
                        "🏆",
                        str(match.points_won)
                        + "/"
                        + str(match.total_points),
                        "Points Won"
                    ),

                    stat_card(
                        "❌",
                        str(match.errors),
                        "Errors"
                    ),

                    stat_card(
                        "⚡",
                        str(match.successful_smashes)
                        + "/"
                        + str(match.total_smashes),
                        "Successful Smashes"
                    ),

                    stat_card(
                        "🎯",
                        str(match.successful_serves)
                        + "/"
                        + str(match.total_serves),
                        "Successful Serves"
                    ),

                    classes="stat-grid"
                ),

                classes="match-card"
            )
        )

        match_number += 1

    content.append(
        Div(

            Button("+ Record Match", record_match),

            Button("📊 Statistics", statistics),

            Button(
                "← Back to Home",
                index,
                classes="secondary-button"
            ),

            classes="navigation"
        )
    )

    content.append(footer())

    # Advanced technique: Argument unpacking.
    # The * operator passes each component in the
    # content list to Div as a separate argument.
    # This allows the page to display any number
    # of dynamically generated match cards.

    return Page(state, [
        Div(
            *content,
            classes="dashboard"
        )
    ])


# ==========================================
# ROUTE 5: PERFORMANCE STATISTICS
# ==========================================

@route
def statistics(state: State) -> Page:

    # Prevent division by zero when no matches
    # have been recorded.

    if len(state.matches) == 0:

        return Page(state, [
            Div(

                topbar(),

                Div(
                    Header("📊 Performance Statistics"),

                    Div(
                        "Discover your strengths and "
                        "track your improvement.",
                        classes="hero-description"
                    ),

                    classes="hero"
                ),

                Div(
                    Div("📈", classes="stat-icon"),

                    Header("No Statistics Yet", 2),

                    Div(
                        "Record your first match to "
                        "unlock your performance statistics."
                    ),

                    Button(
                        "Record Match",
                        record_match
                    ),

                    classes="empty-card"
                ),

                Button(
                    "← Back to Home",
                    index,
                    classes="secondary-button"
                ),

                footer(),

                classes="dashboard"
            )
        ])

    # Initialize integer totals.

    points_won = 0
    total_points = 0
    errors = 0
    total_smashes = 0
    successful_smashes = 0
    total_serves = 0
    successful_serves = 0

    # Meaningful loop:
    # Calculate the total statistics by iterating
    # through the Match instances in State.

    for match in state.matches:

        points_won += match.points_won
        total_points += match.total_points
        errors += match.errors
        total_smashes += match.total_smashes
        successful_smashes += match.successful_smashes
        total_serves += match.total_serves
        successful_serves += match.successful_serves

    # Calculate the point win rate.

    point_rate = points_won / total_points * 100

    # Initialize percentages as floats.
    # This prevents int/float type-checking errors.
    # Check denominators to avoid division by zero.

    smash_rate = 0.0

    if total_smashes > 0:

        smash_rate = (
            successful_smashes / total_smashes * 100
        )

    serve_rate = 0.0

    if total_serves > 0:

        serve_rate = (
            successful_serves / total_serves * 100
        )

    average_errors = errors / len(state.matches)

    # Provide personalized feedback based on
    # the player's point win rate.

    feedback = (
        "Keep practicing and focus on reducing "
        "unforced errors."
    )

    if point_rate >= 50:

        feedback = (
            "Great work! You are winning at least "
            "half of your recorded points. "
            "Keep building your consistency."
        )

    # Display the calculated performance statistics.

    return Page(state, [
        Div(

            topbar(),

            Div(
                Div(
                    "PERFORMANCE ANALYTICS",
                    classes="eyebrow"
                ),

                Header("📊 Performance Statistics"),

                Div(
                    "Understand your game. "
                    "Improve one match at a time.",
                    classes="hero-description"
                ),

                classes="hero"
            ),

            Div(

                stat_card(
                    "🏆",
                    str(len(state.matches)),
                    "Total Matches"
                ),

                stat_card(
                    "📈",
                    str(round(point_rate, 1)) + "%",
                    "Point Win Rate"
                ),

                stat_card(
                    "❌",
                    str(round(average_errors, 1)),
                    "Average Errors"
                ),

                classes="stat-grid"
            ),

            # Point performance

            Div(
                Header("🏆 Point Performance", 2),

                Div(
                    "Points Won: "
                    + str(points_won)
                    + "/"
                    + str(total_points)
                ),

                Div(
                    str(round(point_rate, 2)) + "%",
                    classes="stat-value"
                ),

                progress_bar(point_rate),

                Div(
                    "Percentage of all recorded "
                    "points won."
                ),

                classes="section-card"
            ),

            # Smash performance

            Div(
                Header("⚡ Smash Performance", 2),

                Div(
                    "Successful Smashes: "
                    + str(successful_smashes)
                    + "/"
                    + str(total_smashes)
                ),

                Div(
                    str(round(smash_rate, 2)) + "%",
                    classes="stat-value"
                ),

                progress_bar(smash_rate),

                Div(
                    "Percentage of smashes that "
                    "were successful."
                ),

                classes="section-card"
            ),

            # Serve performance

            Div(
                Header("🎯 Serve Performance", 2),

                Div(
                    "Successful Serves: "
                    + str(successful_serves)
                    + "/"
                    + str(total_serves)
                ),

                Div(
                    str(round(serve_rate, 2)) + "%",
                    classes="stat-value"
                ),

                progress_bar(serve_rate),

                Div(
                    "Percentage of serves that "
                    "were successful."
                ),

                classes="section-card"
            ),

            # Error performance

            Div(
                Header("❌ Error Statistics", 2),

                Div(

                    stat_card(
                        "📋",
                        str(errors),
                        "Total Errors"
                    ),

                    stat_card(
                        "📉",
                        str(round(average_errors, 2)),
                        "Average Errors per Match"
                    ),

                    classes="stat-grid"
                ),

                classes="section-card"
            ),

            # Personalized performance feedback

            Div(
                Header("💪 Performance Feedback", 2),

                Div(feedback),

                Div(
                    "Your training goal: " + state.goal
                ),

                classes="tip-card"
            ),

            Div(

                Button("📋 Match History", match_history),

                Button("+ Record Match", record_match),

                Button(
                    "← Back to Home",
                    index,
                    classes="secondary-button"
                ),

                classes="navigation"
            ),

            footer(),

            classes="dashboard"
        )
    ])


# ==========================================
# ROUTE 6: PROFILE PAGE
# ==========================================

@route
def profile(state: State) -> Page:

    return Page(state, [
        Div(

            topbar(),

            Div(
                Div(
                    "PLAYER PROFILE",
                    classes="eyebrow"
                ),

                Header("👤 My Profile"),

                Header(state.player_name, 2),

                Div(
                    "Your game. Your goals. Your journey.",
                    classes="hero-description"
                ),

                classes="hero"
            ),

            # Player overview

            Div(

                stat_card(
                    "🏆",
                    str(len(state.matches)),
                    "Matches Recorded"
                ),

                stat_card(
                    "⚡",
                    state.favorite_shot,
                    "Favorite Shot"
                ),

                classes="stat-grid"
            ),

            # Editable player information

            Div(
                Header("Player Information", 2),

                Div(
                    "Player Name",
                    classes="field-label"
                ),

                TextBox(
                    "player_name",
                    state.player_name
                ),

                Div(
                    "Training Goal",
                    classes="field-label"
                ),

                TextBox(
                    "goal",
                    state.goal
                ),

                Div(
                    "Favorite Shot",
                    classes="field-label"
                ),

                SelectBox(
                    "favorite_shot",
                    [
                        "Smash",
                        "Drop Shot",
                        "Clear",
                        "Drive",
                        "Net Shot"
                    ],
                    state.favorite_shot
                ),

                classes="section-card"
            ),

            Div(
                Header("🎯 Current Training Goal", 2),

                Div(state.goal),

                classes="tip-card"
            ),

            Div(

                Button("✓ Save Profile", save_profile),

                Button(
                    "← Back to Home",
                    index,
                    classes="secondary-button"
                ),

                classes="navigation"
            ),

            footer(),

            classes="dashboard"
        )
    ])


# ==========================================
# ROUTE 7: SAVE PROFILE
# ==========================================

@route
def save_profile(
    state: State,
    player_name: str,
    goal: str,
    favorite_shot: str
) -> Page:

    # Validate the player's name.

    if player_name.strip() == "":

        return Page(state, [
            Div(

                topbar(),

                Div(
                    Header("⚠ Invalid Input"),

                    Div("Please enter your name."),

                    Button("Back to Profile", profile),

                    classes="error-card"
                ),

                footer(),

                classes="dashboard"
            )
        ])

    # Validate the training goal.

    if goal.strip() == "":

        return Page(state, [
            Div(

                topbar(),

                Div(
                    Header("⚠ Invalid Input"),

                    Div(
                        "Please enter a training goal."
                    ),

                    Button("Back to Profile", profile),

                    classes="error-card"
                ),

                footer(),

                classes="dashboard"
            )
        ])

    # Meaningfully modify State fields 2, 3, and 4.

    state.player_name = player_name.strip()
    state.goal = goal.strip()
    state.favorite_shot = favorite_shot

    return Page(state, [
        Div(

            topbar(),

            Div(
                Div("✓", classes="stat-icon"),

                Header("Profile Updated!"),

                Div(
                    "Your profile has been "
                    "successfully saved."
                ),

                classes="success-card"
            ),

            Div(
                Header("👤 Your Player Profile", 2),

                Div(
                    "Player Name: " + state.player_name
                ),

                Div(
                    "Training Goal: " + state.goal
                ),

                Div(
                    "Favorite Shot: " + state.favorite_shot
                ),

                classes="section-card"
            ),

            Div(

                Button("Edit Profile", profile),

                Button(
                    "← Back to Home",
                    index,
                    classes="secondary-button"
                ),

                classes="navigation"
            ),

            footer(),

            classes="dashboard"
        )
    ])


# ==========================================
# START SERVER
# ==========================================

# The State instance is passed directly to
# start_server, so no global state variable
# is needed.

start_server(State(
    [],
    "Player",
    "Improve my badminton skills",
    "Smash"
))
