# Daily Routine Tracker

A mobile-first routine tracker packaged as an Android app with Capacitor.

## What's updated
- First-run profile setup: name, age, religion, city, and country.
- Religion-aware visual theme; prayer features are shown for Muslim profiles.
- Online prayer-time calculation using the AlAdhan prayer-times API, with manual editing and a reminder-friendly schedule.
- Separate Today, Study, Goals, Prayer, and More screens.
- Today's study plan and study-time analysis.
- Custom goals with progress tracking and a progress summary.
- Activity status includes **Done, but late**; activity replacement and rescheduling remain available.
- Existing local data, reminders, calendar, statistics, and JSON backup/import are retained.

## Build an APK with GitHub Actions
1. Upload/extract the project into a GitHub repository, keeping the `.github/workflows/done.yml` path.
2. Push to `main` or `master`, or open **Actions → Build Daily Routine Tracker APK → Run workflow**.
3. Open the completed workflow run and download the `Daily-Routine-Tracker-APK` artifact.
4. Extract the artifact ZIP to get `app-debug.apk`.

This workflow creates an installable **debug APK** and does not require signing secrets. For public distribution, configure a private release keystore and a separate signed-release workflow.

## Prayer times
Prayer times are fetched from the AlAdhan service using the city and country entered in the profile. The returned calculation may differ from local mosque or official timetables. Users should verify local times and can edit the times manually. An internet connection is needed for refreshes; previously saved times remain available offline.

## Local data
Routine records are stored locally in the app/browser storage. Use Settings → Export JSON to make a backup before clearing app data or reinstalling.
