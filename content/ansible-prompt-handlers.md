Title: Ansible 'Prompt' Handlers
Date: 2015-01-02 11:00
Category: Linux
Tags: linux, ansible, tomcat
Slug: ansible-prompt-handlers
Author: James Oguya
Summary: An awesome feature in Chef that is not available in Ansible is immediate notification. Ansible has notification handlers but they are only triggered at the end of the current playbook unlike Chef's which can be triggered immediately! This blogpost describes an easier way of having immediate handlers in ansible.

An awesome feature in [Chef](https://chef.io) that is not available in [Ansible](http://ansible.com) is immediate notification i.e. `notifies :immediately`.
Ansible has [notification handlers](http://docs.ansible.com/playbooks_intro.html#handlers-running-operations-on-change) but they are only triggered at the end of the current playbook unlike [Chef's notifications](https://docs.chef.io/resource_common.html#notifies-syntax) which can be triggered immediately! Moreover, you can configure Chef's notifications to be triggered at specific times e.g. at the very end of a chef-client run i.e. `notifies :delayed` or immediately i.e. `notifies :immediately`.

Now, why I'm going into all these boring theories? Well, when installing tomcat on Ubuntu, dpkg starts it automatically once the process is complete. But in my case, I wanted to stop tomcat7 service first, configure it, deploy its webapps & finally start it. So on my ansible tasks file, after installing tomcat7 I added a notification action to call a task that stops tomcat7 service. Here's a snippet from the ansible task file:

_tomcat.yml_:

    - hosts: all
      sudo: yes
      tasks:
        - name: Install tomcat7
          apt: name={{ item }} install_recommends=no update_cache=yes  state=present
          with_items:
            - tomcat7
            - tomcat7-admin
          notify:
            - Temporarily stop tomcat7

      handlers:
          - name: Temporarily stop tomcat7
          service: name=tomcat7 state=stopped

OK so the task file looks great, but did it work ? Unfortunately, no! Ansible notifications trigger tasks in handlers section to run only at the end of a playbook.
So I had to come up with a quick fix for this issue.

### 'Prompt' handlers

My quick fix involved registering a variable in the task that installs tomcat packages i.e. `register: tomcat_installed`, then the next task to stop tomcat service would be executed only if the registered variable has changed i.e. if tomcat7 has been installed - `when: tomcat_installed|changed`.
Basically, ansible notifications use a similar concept to this.

Here's a snippet from the playbook showing the quick fix:

_tomcat.yml_:

    - hosts: all
      sudo: yes
      tasks:
          - name: Install tomcat7
            apt: name={{ item }} install_recommends=no update_cache=yes state=present
            with_items:
              - tomcat7
              - tomcat7-admin
            register: tomcat_installed

          - name: Temporarily stop tomcat7
            service: name=tomcat7 state=stopped
            when: tomcat_installed|changed

As you can see from the snippet, I've not used a handler. Yes that's right, inorder to achieve the effect of an 'immediate' handler, I moved the task that stops tomcat7 service from the handler section to the tasks section.

### Conclusion
Though I'm sure there are better solutions out there, I think the concept behind my quick fix can be useful in tackling other ansible-related issues.
