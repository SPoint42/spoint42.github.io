---
layout: post
date: 2025-02-27
title: "Quick Notes of the day - 27th February 2025"
description: "Quick notes of the day - 27th February 2025"
category: QuickNotes
---
Here are the quick notes of the day:

## 📚 Splunk Query to Quickly Check for Anomalous Scanning Activity

Vérifier rapidement que vous avez des gens qui vous reniflent de manière anormale et afficher dans splunk sur une carte 
geographique

```splunk
index=monsuperindex ("RequestPath"="*%00*" OR RequestPath="*/etc/*" OR requestPath="*.exe*") clientip NOT  my.ip.a.moi| iplocation clientip| geostats count
```