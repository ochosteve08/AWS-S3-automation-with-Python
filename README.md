# 🛠️ S3 Automation with Python

This repository contains Python scripts for automating common AWS S3 tasks using the `boto3` SDK. The scripts allow you to **list, create, upload, delete, and organize S3 buckets and objects** in an automated manner.

This repository contains a collection of Python scripts for automating various Amazon S3 operations. The scripts leverage the `<span>boto3</span>` library to interact with AWS S3 and perform common tasks such as listing, uploading, downloading, creating, deleting, and managing buckets and objects.

## 🚀 Features

* 🏗️ **Create S3 Buckets** – Automates the creation of new S3 buckets.
* 📁 **Create Subfolders in S3** – Simulate folder structures inside an S3 bucket.
* 🔍 **List Objects in a Bucket** – Fetch details of objects stored in a specific S3 bucket.
* 📝 **Logging Support** – Tracks execution details, errors, and warnings.
* 📤 **Upload Files to S3** – Enables easy uploading of files to a specified S3 bucket.
* 🗑️ **Delete Files from S3** – Removes single or multiple files from an S3 bucket.
* 📥 **Download Files from S3** – Fetch files from an S3 bucket to your local machine.
* 🏗️ **Delete Multiple Files in S3** – Supports batch deletion of multiple files within a bucket.
* 🚮 **Delete S3 Bucket** – Deletes an empty S3 bucket.
* 🏗️ **Delete S3 Bucket and All Object Versions** – Removes a bucket along with all its objects and versions.
* 🔥 **Delete Multiple Buckets and All Object Versions** – Batch deletion of multiple S3 buckets, including all objects and versions.
* 📂 **Delete Folder in S3** – Deletes a folder and its contents within a bucket.

## 🔧 Prerequisites

Ensure you have the following before running the scripts:

* **Python 3.x +** installed
* **AWS CLI** installed and configured (`<span>aws configure</span>`)
* **Boto3 library** installed (`<span>pip install boto3</span>`)
* Proper IAM permissions to interact with S3, AWS credentials configured in `<span>~/.aws/credentials</span>` or environment variables

## 🚀 Installation

1. Clone this repository:

   ```sh
   git clone https://github.com/ochosteve08/AWS-S3-automation-with-Python.git
   ```

## 🚀 Usage

Each script is a standalone executable Python file. Run them with:

```
python script_name.py
```


## 📝 Logging

Each script logs its actions for debugging and auditing. Logs are stored in `<span>s3_automation.log</span>`.


## ⚠️ Notes

* Ensure your **AWS IAM role** has the necessary permissions (`s3:ListBucket`, `s3:PutObject`, `s3:DeleteObject`, `s3:DeleteBucket`).
* When deleting a bucket,  **all objects (including versions) must be deleted first** .
* The scripts handle basic error checking but may need adjustments based on your AWS setup.
* **Logging** is implemented in most scripts for better debugging.


## 🤝 Contributing

Feel free to submit issues or pull requests to improve the project.

## 📜 License

This project is licensed under the MIT License.


## 👨‍💻 Author

**Ujah Stephen Ocheola**

📧 [stephenujah@yahoo.com](mailto:stephenujah@yahoo.com)
