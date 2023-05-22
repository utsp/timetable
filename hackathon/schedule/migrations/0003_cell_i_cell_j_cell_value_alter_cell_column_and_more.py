# Generated by Django 4.2.1 on 2023-05-21 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("schedule", "0002_timeslot_end_hour_timeslot_end_minute_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cell",
            name="i",
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="cell",
            name="j",
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="cell",
            name="value",
            field=models.SmallIntegerField(
                choices=[(-1, -1), (0, 0), (1, 1)], default=1
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="cell",
            name="column",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cell",
                to="schedule.column",
            ),
        ),
        migrations.AlterField(
            model_name="cell",
            name="row",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cell",
                to="schedule.row",
            ),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="end_hour",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, 0),
                    (1, 1),
                    (2, 2),
                    (3, 3),
                    (4, 4),
                    (5, 5),
                    (6, 6),
                    (7, 7),
                    (8, 8),
                    (9, 9),
                    (10, 10),
                    (11, 11),
                    (12, 12),
                    (13, 13),
                    (14, 14),
                    (15, 15),
                    (16, 16),
                    (17, 17),
                    (18, 18),
                    (19, 19),
                    (20, 20),
                    (21, 21),
                    (22, 22),
                    (23, 23),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="end_minute",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, 0),
                    (1, 1),
                    (2, 2),
                    (3, 3),
                    (4, 4),
                    (5, 5),
                    (6, 6),
                    (7, 7),
                    (8, 8),
                    (9, 9),
                    (10, 10),
                    (11, 11),
                    (12, 12),
                    (13, 13),
                    (14, 14),
                    (15, 15),
                    (16, 16),
                    (17, 17),
                    (18, 18),
                    (19, 19),
                    (20, 20),
                    (21, 21),
                    (22, 22),
                    (23, 23),
                    (24, 24),
                    (25, 25),
                    (26, 26),
                    (27, 27),
                    (28, 28),
                    (29, 29),
                    (30, 30),
                    (31, 31),
                    (32, 32),
                    (33, 33),
                    (34, 34),
                    (35, 35),
                    (36, 36),
                    (37, 37),
                    (38, 38),
                    (39, 39),
                    (40, 40),
                    (41, 41),
                    (42, 42),
                    (43, 43),
                    (44, 44),
                    (45, 45),
                    (46, 46),
                    (47, 47),
                    (48, 48),
                    (49, 49),
                    (50, 50),
                    (51, 51),
                    (52, 52),
                    (53, 53),
                    (54, 54),
                    (55, 55),
                    (56, 56),
                    (57, 57),
                    (58, 58),
                    (59, 59),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="start_hour",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, 0),
                    (1, 1),
                    (2, 2),
                    (3, 3),
                    (4, 4),
                    (5, 5),
                    (6, 6),
                    (7, 7),
                    (8, 8),
                    (9, 9),
                    (10, 10),
                    (11, 11),
                    (12, 12),
                    (13, 13),
                    (14, 14),
                    (15, 15),
                    (16, 16),
                    (17, 17),
                    (18, 18),
                    (19, 19),
                    (20, 20),
                    (21, 21),
                    (22, 22),
                    (23, 23),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="start_minute",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, 0),
                    (1, 1),
                    (2, 2),
                    (3, 3),
                    (4, 4),
                    (5, 5),
                    (6, 6),
                    (7, 7),
                    (8, 8),
                    (9, 9),
                    (10, 10),
                    (11, 11),
                    (12, 12),
                    (13, 13),
                    (14, 14),
                    (15, 15),
                    (16, 16),
                    (17, 17),
                    (18, 18),
                    (19, 19),
                    (20, 20),
                    (21, 21),
                    (22, 22),
                    (23, 23),
                    (24, 24),
                    (25, 25),
                    (26, 26),
                    (27, 27),
                    (28, 28),
                    (29, 29),
                    (30, 30),
                    (31, 31),
                    (32, 32),
                    (33, 33),
                    (34, 34),
                    (35, 35),
                    (36, 36),
                    (37, 37),
                    (38, 38),
                    (39, 39),
                    (40, 40),
                    (41, 41),
                    (42, 42),
                    (43, 43),
                    (44, 44),
                    (45, 45),
                    (46, 46),
                    (47, 47),
                    (48, 48),
                    (49, 49),
                    (50, 50),
                    (51, 51),
                    (52, 52),
                    (53, 53),
                    (54, 54),
                    (55, 55),
                    (56, 56),
                    (57, 57),
                    (58, 58),
                    (59, 59),
                ],
                default=0,
            ),
        ),
    ]