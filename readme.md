# Odoo Hospital Management System Addon

This custom Odoo addon is designed for managing hospital operations, including managing patients, scheduling appointments, and more. The module extends Odoo's capabilities to cater specifically to hospital and clinic requirements.

## Features

- **Patient Management**:

  - Add, edit, and view patient records.
  - Maintain detailed patient profiles, including contact details, medical history, and more.

- **Appointment Management**:

  - Schedule appointments for patients with doctors.
  - View and manage all appointments.
  - Track appointment status (e.g., Scheduled, Completed, Canceled).

- **Doctor Management**:
  - Associate doctors with appointments.
  - Manage doctor availability and schedules.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/odoo-hospital-addon.git
   ```

2. Copy the addon folder into your Odoo addons directory.

3. Restart the Odoo server:

   ```bash
   ./odoo-bin -u all
   ```

4. Activate developer mode in Odoo and navigate to **Apps**.

5. Update the app list and search for "Hospital Management System." Install the module.

## Usage

1. Go to the **Hospital** menu in Odoo after installing the module.

2. Use the **Patients** submenu to add and manage patient records.

3. Schedule appointments via the **Appointments** submenu by selecting a patient and assigning a doctor.

4. Use the **Doctors** submenu to manage doctor information and availability.

## Screenshots

![Dashboard](path/to/dashboard-screenshot.png)
_Caption: Hospital Management Dashboard_

![Patient Management](path/to/patient-management-screenshot.png)
_Caption: Patient Management Interface_

![Appointment Management](path/to/appointment-management-screenshot.png)
_Caption: Appointment Scheduling_

## Dependencies

- Odoo 15 or later.
- Python dependencies:
  - `pandas`
  - `xlrd`

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact:

- **Author**: [Your Name]
- **Email**: your.email@example.com
- **GitHub**: [your-username](https://github.com/your-username)

---

Thank you for using the Odoo Hospital Management System addon! We welcome feedback and suggestions to improve the module.
