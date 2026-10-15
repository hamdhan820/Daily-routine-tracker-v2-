f = 'android/app/src/main/AndroidManifest.xml'
s = open(f).read()

def must_replace(s, old, new, count=1):
    if old not in s:
        raise SystemExit('PATCH FAILED, not found in manifest: ' + old)
    return s.replace(old, new, count)

perms = ''.join('<uses-permission android:name="android.permission.%s" />\n' % p for p in
  ['SCHEDULE_EXACT_ALARM', 'USE_EXACT_ALARM', 'POST_NOTIFICATIONS', 'USE_FULL_SCREEN_INTENT', 'WAKE_LOCK', 'VIBRATE', 'RECEIVE_BOOT_COMPLETED'])
s = must_replace(s, '<application', perms + '<application')

# Security hardening: no backups of app data, no plain-HTTP traffic
s = must_replace(s, 'android:allowBackup="true"', 'android:allowBackup="false"')
if 'usesCleartextTraffic' not in s:
    s = must_replace(s, '<application', '<application android:usesCleartextTraffic="false"')

# Never ship a debuggable build
if 'android:debuggable' in s:
    raise SystemExit('PATCH FAILED: manifest must not set android:debuggable')

s = must_replace(s, '</application>', '<activity android:name=".AlarmActivity" android:exported="false" android:showWhenLocked="true" android:turnScreenOn="true" android:excludeFromRecents="true" android:launchMode="singleTask" />\n<receiver android:name=".AlarmReceiver" android:exported="false" />\n</application>')
open(f, 'w').write(s)
print('manifest patched')
