# This file is part of OpenHatch.
# Copyright (C) 2010 John Stumpo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.db import models

class Step(models.Model):
    name = models.CharField(max_length=255, unique=True)

class StepCompletion(models.Model):
    person = models.ForeignKey('profile.Person')
    step = models.ForeignKey('Step')
    # Current mission status (True - user have completed it, False - reseted) 
    is_currently_completed = models.BooleanField(default=True)
	
    class Meta:
        unique_together = ('person', 'step')
