# File Storage System Design

## Purpose
Design a file storage system that allows users to upload, download, delete, and organize files and folders while tracking storage usage and enforcing quotas.

## Core Requirements
- Upload, download, and delete files.
- Organize files into folders.
- Support nested folders, where a folder may contain files and subfolders.
- Store metadata for each file: name, size, type, and content.
- Search for files by name.
- Track storage usage per user and enforce a storage limit.

## Constraints
- Files cannot contain other files or folders; only folders can contain children.
- Each user receives a maximum storage quota (for example, 15GB).
- File and folder names must be unique within the same parent folder.
- Only the owner may delete or modify their files and folders.

## Possible Extensions
- Add folder sharing or access control lists.
- Support file rename and move operations.
- Add version history for files.
- Add storage reporting and quota alerts.
- Support file metadata tags, timestamps, and type-specific indexing.
